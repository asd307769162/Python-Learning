import urllib.request
import urllib.error
from urllib.error import URLError,HTTPError


req=Request(someurl)

try:
    response=urlopen(req)
except URLError as e:
    if hasattr(e,'reason'):
        print('We failed to reach a server.')
        print('Reason:',e.reason)
    elif hasattr(e,'code'):
        print('The server could not fulfill the request.')
        print('Error code:',e.code)
else:
# everything is fine.

