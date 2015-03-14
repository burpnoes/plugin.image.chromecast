# -*- coding: utf-8 -*-
import sys
import simplejson
import urllib2

import xbmcgui
import xbmcplugin

CHANNELS_URL = 'http://chromecastbg.alexmeub.com/images.v4.json'

def showPictures():
    u = urllib2.urlopen(CHANNELS_URL)
    data = u.read()
    u.close()

    result = simplejson.loads(data)
    pictures = result

    for picture in pictures:

        item = xbmcgui.ListItem(picture['name'], iconImage = 'http://chromecastbg.alexmeub.com/images/240_' + picture['name'])

        itm.setInfo('pictures', {
            'title': 'By ' + picture['photographer']
        });

        xbmcplugin.addDirectoryItem(HANDLE, 'http://chromecastbg.alexmeub.com/images/1080_' + picture['name'], item)

    xbmcplugin.endOfDirectory(HANDLE)

if __name__ == '__main__':
    HANDLE = int(sys.argv[1])
    showPictures()

