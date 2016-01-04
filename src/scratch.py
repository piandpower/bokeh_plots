from urlparse import urlparse
from data import data
from collections import Counter


urls = [x[0][0] for x in data["pages"]]
xdata = [x[1] for x in data["pages"]]
ydata = [x[2] for x in data["pages"]]

domains = [urlparse(x).hostname for x in urls]
endings = [x[x.rfind("."):] for x in domains]

print(Counter(domains))
print(Counter(endings))
