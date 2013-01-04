#!/usr/bin/perl -w
# nagios: +epn
################################################################################
## Nagios notification script (send states to Vigilo)
##
## Copyright (C) 2007-2013 CS-SI
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#################################################################################

# Do the equivalent of:
# /usr/bin/printf "%b" \
#   "state|$TIMET$|$HOSTNAME$|$SERVICEDESC$|$SERVICESTATE$|$SERVICEOUTPUT$\\n" \
#   | socat -u - UNIX-CONNECT:/var/lib/vigilo/connector-nagios/send.sock

package nagios2vigilo;
my(%ERRORS) = ( OK=>0, WARNING=>1, CRITICAL=>2, UNKNOWN=>3, WARN=>1, CRIT=>2 );

use POSIX;
use Getopt::Long;
use strict;
use IO::Socket::UNIX;
#####################################################################
sub print_usage () {
    print "Usage: nagios2vigilo [--state|--event] [--socket /patch/to/connector-nagios/send.sock] ARGS\n";
    print "       nagios2vigilo --state \$TIMET\$ \$HOSTNAME\$ \$HOSTADDRESS\$ \$SERVICEDESC\$ \$SERVICESTATEID\$ \$SERVICESTATETYPE\$ \$SERVICEATTEMPT\$ \$SERVICEOUTPUT\$\n";
    print "       nagios2vigilo --state \$TIMET\$ \$HOSTNAME\$ \$HOSTADDRESS\$ '' \$HOSTSTATEID\$ \$HOSTSTATETYPE\$ \$HOSTATTEMPT\$ \$HOSTOUTPUT\$\n";
    print "       nagios2vigilo --event \$TIMET\$ \$HOSTNAME\$ \$SERVICEDESC\$ \$SERVICESTATE\$ \$SERVICEOUTPUT\$ \$SERVICESTATETYPE\$\n" ;
    print "       nagios2vigilo --event \$TIMET\$ \$HOSTNAME\$ '' \$HOSTSTATE\$ \$HOSTOUTPUT\$ \$HOSTSTATETYPE\$\n" ;
}

sub print_help () {
    print "Nagios to Vigilo notification script\n";
    print "Copyright (C) 2007-2011 CS-SI\n";
    print "This plugin transmits event or state to Vigilo\n\n";
    print_usage();
}

my $opt_h = 0;
my $debug = 0;
my $event = 0;
my $state = 0;
my $connector_socket = "/var/lib/vigilo/connector-nagios/send.sock";

Getopt::Long::Configure('bundling');
GetOptions
    ("h" => \$opt_h,  "help"     => \$opt_h,
     "d" => \$debug,  "debug"    => \$debug,
     "e" => \$event,  "event"    => \$event,
     "s" => \$state,  "state"    => \$state,
     "S=s" => \$connector_socket, "socket=s" => \$connector_socket );

my $nb_param = scalar @ARGV;
my $message;

if ($opt_h) {
    print_help(); exit $ERRORS{'UNKNOWN'};
}

if ( $event && $nb_param eq 6) {
    $message = "event";
    # Nagios peut envoyer une notification pour un SOFT state
    # lorsqu'on force l'envoi d'une notification.
    # On ne traite que les HARD states dans ce script.
    if (lc(pop(@ARGV)) eq "soft") {
        return;
    }

} elsif ( $state && $nb_param eq 8) {
    $message = "state";

} else {
    print_help(); exit $ERRORS{'UNKNOWN'};
}

foreach my $arg ( @ARGV ) {
    $message = $message . "|" . $arg ;
}
$message = $message . "\n" ;



my $sock = IO::Socket::UNIX->new( Type => IO::Socket::SOCK_STREAM, Peer => $connector_socket) or die ("error while trying to open socket to $connector_socket");
$sock->send("$message");
print "nagios2vigilo : $message" if ($debug);
$sock->close();

