import socket
from urllib2 import urlopen, URLError, HTTPError

socket.setdefaulttimeout( 23 )  # timeout in seconds

url = 'http://music.xbox.com'
try :
    response = urlopen( url )
except HTTPError, e:
    xbmc.executebuiltin('Skin.SetString(MusicStatus, DOWN:' + str(e.code) +')')
except URLError, e:
    xbmc.executebuiltin('Skin.SetString(MusicStatus, DOWN:' + str(e.reason) +')')
else :
    html = response.read()
    xbmc.executebuiltin('Skin.SetString(MusicStatus, UP)')
    # do something, turn the light on/off or whatever