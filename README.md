# findDomainsTraceroute
Gets the names of the domains that is found in a traceroute. Gives the path of a traceroute in terms of the internet domains it crosses.

Usage: ./getPath.sh <destination IP address>
Make sure that the destination IP address is reachable in the first place.
Dependencies:
1. Install phantomjs-1.9.8-linux-x86_64.tar.bz2
2. Install selenium in python
3. Install BeautifulSoup in python
4. Change browser executable path in "getDomains.py" to the location of "phantomjs".
