use strict;
use warnings;

use Data::Dumper;

package DataTree;

use Carp                qw(confess);
use Params::Validate    qw(validate UNDEF BOOLEAN SCALAR ARRAYREF HASHREF OBJECT);

sub new {
    my $class = shift;
    my %opts = validate(@_, {
        data_rows_AOH   => {type => ARRAYREF},
        select_columns  => {type => ARRAYREF},
        aggr_colums     => {type => ARRAYREF}
    });
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

sub get_data_rows {
    my $self = shift;
    return $self->{'data_rows_AOH'};
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


package main;

my @group_by_data = ();
my $level = 0;
my $distinct = 1;
sub _get_instance_count {
    my $prev_key = shift;
    my $max_level = shift;
    my $data = shift;
    foreach my $k(keys(%{$data})) {
        my $prefix;
        if($prev_key) {
            $prefix = $prev_key."->".$k;
            $level += 1;
        }else {
            $prefix = $k;
            $level = 0;
        }
        if($level == ($max_level-1)) {
            $prev_key .= "->$k##";
            while(my ($k, $v) = each(%{$data->{$k}})) {
                if($distinct) {
                    my %vals = map{$_ =>}@{$v};
                    $prev_key .= "~~$k=".scalar(keys(%vals));
                }else {
                    $prev_key .= "~~$k=".scalar(@{$v});
                }
            }
            return $prev_key;
        }
        my $l = _get_instance_count($prefix, $max_level, $data->{$k});
        $level -= 1;
        if($l ne 'not_reached_count') {
            push(@group_by_data, $l) ;
        }
    }
    return "not_reached_count";
}

sub main {
    my @data_rows = (
        {'region' => 'region1', 'user_name' => 'user1', 'type' => 'm2.large', 'state' => 'running', 'id' => 'id1'},
        {'region' => 'region1', 'user_name' => 'user1', 'type' => 'm2.large', 'state' => 'stopped', 'id' => 'id2'},
    );
    my @select_columns = ('region', 'user_name');
    my $dt = DataTree->new(
        data_rows_AOH   => \@data_rows,
        select_columns  => \@select_columns,
        aggr_colums     => ['id', 'state', 'type']
    );
    my $dtrs = $dt->get_data_rows();
    print "get_data_rows:\n".Dumper($dt)."\n";
    $dt->_construct_data_tree();
    print "data_tree:\n".Dumper($dt->{'data_tree'})."\n";

    _get_instance_count(undef, scalar(@select_columns), $dt->{'data_tree'});
    print "group_by_data:\n".Dumper(\@group_by_data);
}

main();