# -*- coding: utf-8 -*-
import sys
import simplejson
import urllib2

import xbmcgui
import xbmcplugin

SERVICE_URL = 'http://chromecastbg.alexmeub.com'

CHANNELS_URL = SERVICE_URL + '/images.v4.json'

def showPictures():
    u = urllib2.urlopen(CHANNELS_URL)
    data = u.read()
    u.close()

    result = simplejson.loads(data)
    pictures = result

    for picture in pictures:

        item = xbmcgui.ListItem(picture['name'], iconImage = SERVICE_URL + '/images/240_' + picture['name'])

        item.setInfo('pictures', {
            'title': 'By ' + picture['photographer']
        });

        full_image_path = '/images/1080_'

        xbmcplugin.addDirectoryItem(HANDLE, SERVICE_URL + full_image_path + picture['name'], item)

    xbmcplugin.endOfDirectory(HANDLE)

if __name__ == '__main__':
    HANDLE = int(sys.argv[1])
    showPictures()

