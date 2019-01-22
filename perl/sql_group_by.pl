use strict;

use Data::Dumper;

my %data = (
    'region1' => 
        {
            'user1' => {'m2.large' => { 'running' => [1,2] }}, 
            'user2' => {'m2.large' => {'stopped' => [1]    }}
            
        }
);

my @group_by_data = ();
sub _get_instance_count {
    my $prev_key = shift;
    my $data = shift;
    if(ref($data) eq 'ARRAY') {
        return $prev_key."=".scalar(@{$data});
    }
    foreach my $k(keys(%{$data})) {
        my $prefix;
        if($prev_key) {
            $prefix = $prev_key."->".$k;
        }else {
            $prefix = $k;
        }
        my $l = _get_instance_count($prefix, $data->{$k});
        if($l ne 'not_reached_count') {
            push(@group_by_data, $l) ;
        }
    }
    return "not_reached_count";
}

_get_instance_count(undef, \%data);
print "group_by_data:\n".Dumper(\@group_by_data);
