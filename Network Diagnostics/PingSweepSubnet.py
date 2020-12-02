# You will pass in a network address and a subnet mask and this application will report IP addressses with successful pings. 

# Add config file with options to do DNS lookups, change ping port #, and do path pings.

# Add functionality for additional scanning layers. (Potentially network mapping)

import pythonping as p
import ipaddress as ip
import sys

# Perform a basic ping of your loopback address with regular output.

test = p.ping('127.0.0.1', count=10)
print(test.success)

# parameters: size(bytes), timout(seconds), count(# of pings), out(defines a location to send verbose data, def sys.stdout)

def pingSweep(cidrNetwork = None, numPings = 4, pingTimeout = 0.15, pingSize = 9, pingOut = sys.stdout):

    for x in ip.ip_network(cidrNetwork):
        response = p.ping(str(x), count=numPings, timeout = pingTimeout, size = pingSize, out = pingOut)
        for y in range(numPings):

            if response._responses[y].success == True:
                print(x)
                break
            else:
                continue

pingSweep(cidrNetwork='73.0.0.0/8', pingTimeout= 0.03, numPings = 2) # Enter desired network here and run. 73.0.0.0/8 is Comcast btw
