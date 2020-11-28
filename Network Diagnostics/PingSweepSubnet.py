# You will pass in a network address and a subnet mask and this application will report IP addressses with successful pings. 

# Add config file with options to do DNS lookups, change ping port #, and do path pings.

# Add functionality for additional scanning layers. (Potentially network mapping)

from pythonping import ping

# Perform a basic ping of your loopback address with regular output.

q = ping('127.0.0.1', verbose=True)

# parameters: size(bytes), timout(seconds), count(# of pings), out(defines a location to send verbose data, def sys.stdout)