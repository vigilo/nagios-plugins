#!/usr/bin/perl -w
# nagios: +epn
################################################################################
## Nagios notification script (send events to Vigilo)
##
## Copyright (C) 2007-2011 CS-SI
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
#   "event|$TIMET$|$HOSTNAME$|$SERVICEDESC$|$SERVICESTATE$|$SERVICEOUTPUT$\\n" \
#   | socat -u - UNIX-CONNECT:/var/lib/vigilo/connector-nagios/send.sock

package event2vigilo;

use POSIX;
use strict;
use IO::Socket::UNIX;

my $debug = 0;

my $help_msg = <<HELPMSG;
Nagios notification script (send events to Vigilo)
Usage:
event2vigilo \$TIMET\$ \$HOSTNAME\$ \$SERVICEDESC\$ \$SERVICESTATE\$ \$SERVICEOUTPUT\$ /var/lib/vigilo/connector-nagios/send.sock
event2vigilo \$TIMET\$ \$HOSTNAME\$ Host \$HOSTSTATE\$ \$HOSTOUTPUT\$ /var/lib/vigilo/connector-nagios/send.sock
HELPMSG

my $nb_param = scalar @ARGV;
if ($nb_param ne 6) {
    print $help_msg;
    exit;
}


my $connector_socket = $ARGV[5];
my $message = "event|".$ARGV[0]."|".$ARGV[1]."|".$ARGV[2]."|".$ARGV[3]."|".$ARGV[4]."\n";
my $sock = IO::Socket::UNIX->new( Type => IO::Socket::SOCK_STREAM, Peer => $connector_socket) or die ("error while trying to open socket to $connector_socket");
$sock->send("$message");
print "event2vigilo : $message" if ($debug);
$sock->close();

