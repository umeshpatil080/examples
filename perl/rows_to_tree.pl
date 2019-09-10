use strict;
use warnings;

use Data::Dumper;
use Sam;

package DataTree;

use Carp                qw(confess);
use Params::Validate    qw(validate UNDEF BOOLEAN SCALAR ARRAYREF HASHREF OBJECT);
use Data::Dumper;

sub new {
    my $class = shift;
    my %opts = validate(@_, {
        data_rows_AOH   => {type => ARRAYREF},
        select_columns  => {type => ARRAYREF},
        aggr_colums     => {type => ARRAYREF}
    });
    # TODO: Validation about column selection and aggr_columns
    if(scalar(@{$opts{'data_rows_AOH'}})){
        my @columns = ();
        foreach my $c(keys(%{$opts{'data_rows_AOH'}->[0]})) {
            push(@columns, $c);
            $opts{'columns'} = \@columns;
        }
    }else {
        confess "No rows data found.\n";
    }
    $opts{'data_tree'} = {};
    my $self = bless(\%opts, $class);
    return $self;
}

sub _is_valid_data_row {
    my $self = shift;
    my %opts = validate(@_, {
        row  => {type => HASHREF}
    });
    
    foreach my $c(@{$self->{'columns'}}) {
        if(!exists($opts{'row'}->{$c})) {
            return 0;
        }
    }
    return 1;
}

sub _construct_data_tree {
    my $self = shift;
    my $data_tree = $self->{'data_tree'};
    my %aggr_colums = map{$_ => 1}@{$self->{'aggr_colums'}};
    my @internal_node_columns = @{$self->{'select_columns'}};
    foreach my $row(@{$self->{'data_rows_AOH'}}) {
        if($self->_is_valid_data_row(row => $row)) {
            my $head = $data_tree;
            foreach my $c(@internal_node_columns) {
                my $node_val = $row->{$c};
                if(exists($head->{$node_val})) {
                    $head = $head->{$node_val};
                }else {
                    $head = $head->{$node_val} = {};
                }
            }
            foreach my $key(keys(%aggr_colums)) {
                my $val = $row->{$key};
                push(@{$head->{$key}}, $val);
            }
        }else {
            confess "Invlid data row found.\n";
        }
    }
}

sub select_group_by {
    my $self = shift;
    my %opts = validate(@_, {
        is_distinct => {type => SCALAR},
    });
    my $is_distinct = $opts{'is_distinct'};
    $self->_construct_data_tree();
    print "data_tree:\n".Dumper($self->{'data_tree'})."\n";
    $self->{'group_by_data'} = [];
    $self->{'level'} = 0;
    $self->{'select_columns_depth'} = scalar(@{$self->{'select_columns'}});
    $self->_get_instance_count("", $self->{'data_tree'}, $is_distinct);
    my $group_by_data = delete($self->{'group_by_data'});
    delete($self->{'level'});
    delete($self->{'select_columns_depth'});
    return $group_by_data;
}

sub _get_instance_count {
    my $self = shift;
    my $prev_key = shift;
    my $data = shift;
    my $is_distinct = shift;
    foreach my $val(keys(%{$data})) {
        print "val: $val\n";
        my $prefix = "";
        if($prev_key) {
            $prefix = $prev_key."->".$val;
        }else {
            $prefix = $val;
        }
        my $reached = 0;
        print "select_columns_depth:".$self->{'select_columns_depth'}."\tlevel:".$self->{'level'}."\tprev_key: $prev_key\n";
        if($self->{'level'} == ($self->{'select_columns_depth'}-1)) {
            $reached = 1;
            $prev_key .= "->$val##";
            print "select_columns_depth:".$self->{'select_columns_depth'}."\tlevel:".$self->{'level'}."\tprev_key: $prev_key\n";
            #print "data:".Dumper($data)."\n";
            while(my ($k, $v) = each(%{$data->{$val}})) {
                if($is_distinct) {
                    my %vals = map{$_ => 1}@{$v};
                    $prev_key .= "~~$k=".scalar(keys(%vals));
                }else {
                    $prev_key .= "~~$k=".scalar(@{$v});
                }
            }
            #return $prev_key;
            print "********* prev_key: $prev_key\n";
            push(@{$self->{'group_by_data'}}, $prev_key) ;
        }
        print "reached: $reached\n";
        if(!$reached) {
            $self->{'level'} += 1;
            print "Invoking with val: $val\n";
            my $l = $self->_get_instance_count($prefix, $data->{$val}, $is_distinct);
            $self->{'level'} -= 1;
            if($l ne 'not_reached_count') {
                #push(@{$self->{'group_by_data'}}, $l) ;
            }
        }else {
            print "Going for next after: $val\n";
        }
    }
    return "not_reached_count";
}


package main;

sub main {
    my @data_rows = (
        {'region' => 'region1', 'user_name' => 'user1', 'type' => 'm2.large', 'state' => 'running', 'id' => 'id1'},
        {'region' => 'region1', 'user_name' => 'user2', 'type' => 'm2.large', 'state' => 'stopped', 'id' => 'id2'},
    );
    my @select_columns = ('region', 'user_name');
    my $dt = DataTree->new(
        data_rows_AOH   => \@data_rows,
        select_columns  => \@select_columns,
        aggr_colums     => ['id', 'state', 'type']
    );

    my $result = $dt->select_group_by(is_distinct => 1);
    print "group_by_data:\n".Dumper($result)."\n";
}

main();