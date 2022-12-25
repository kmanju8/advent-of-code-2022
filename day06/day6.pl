use File::Slurp;

my $code = read_file('input.txt');
my $length = 14;

for $i (0..length($code)-$length){
    $section = substr $code, $i, $length;
    if ($section !~ /(?=^[A-Za-z0-9]+$)(.)+.*\1.*/) {
        print $i+$length;
        last
    }
}

