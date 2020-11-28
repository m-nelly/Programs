# You will pass in a network address and a subnet mask and this application will report IP addressses with successful pings. 

# Add config file with options to do DNS lookups, change ping port #, and do path pings.

# Add functionality for additional scanning layers. (Potentially network mapping)

import pythonping as p
import ipaddress as ip

# Perform a basic ping of your loopback address with regular output.

test = p.ping('127.0.0.1', count=10)
print(test._responses[0].success)

# parameters: size(bytes), timout(seconds), count(# of pings), out(defines a location to send verbose data, def sys.stdout)

def pingSweep(startAddress= None, endAddress = None, subnetMask = None, cidrNetwork = None, numPings = 4):

# The purpose of these arguments is to allow the user freedom in how they approach the network. 

    for x in ip.ip_network(cidrNetwork):
        response = p.ping(str(x), count=4, timeout = 0.025)
        for y in range(4):

            if response._responses[y].success == True:
                print(x)
                break
            else:
                continue
        
userNetwork = str(input('Network(CIDR): '))

pingSweep(cidrNetwork=userNetwork)
