#!/usr/bin/perl
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use strict;

print header;
print start_html("Get Form");

# This loop goes through all of the provided variables and prints those variables in the respectable form.
my %form;
foreach my $p (param()) {
    $form{$p} = param($p);
    print "$p = $form{$p}<br>\n";
}

print end_html;

