from urllib.request import urlopen
from urllib.error import *

URL = input("enter a URL: ")

try:
    html = urlopen(URL)


except HTTPError as e:
    print("HTTP error", e)

except URLError as e:
    print("This page does not exist", e)

else:
    print('Yeah, this page exists')