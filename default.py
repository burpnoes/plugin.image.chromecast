# -*- coding: utf-8 -*-
import sys
try:
    import simplejson
except ImportError:
    import json as simplejson
import urllib2

import xbmcgui
import xbmcaddon
import xbmcplugin

SERVICE_URL = 'http://chromecastbg.alexmeub.com'

CHANNELS_URL = SERVICE_URL + '/images.v4.json'

ADDON = xbmcaddon.Addon()
IMAGE_SIZE = ADDON.getSetting('image_size')


def showPictures():

    images_paths = {
        '0': '/images/240_',
        '1': '/images/1080_',
        '2': '/images/1200_'
    }

    u = urllib2.urlopen(CHANNELS_URL)
    data = u.read()
    u.close()

    result = simplejson.loads(data)
    pictures = result

    for picture in pictures:
        name = picture['name']
        iconimage = SERVICE_URL + '/images/240_' + picture['name']
        full_image_path = images_paths[IMAGE_SIZE] if IMAGE_SIZE else images_paths['2']
        url = SERVICE_URL + full_image_path + picture['name']

        item = xbmcgui.ListItem(name, iconImage = "DefaultImage.png", thumbnailImage = iconimage)

        item.setInfo( type = 'image', infoLabels = {"Title": 'By ' + picture['photographer'] })

        xbmcplugin.addDirectoryItem(handle = HANDLE, url=url, listitem=item, isFolder=False, totalItems=0)

    xbmcplugin.endOfDirectory(HANDLE)

if __name__ == '__main__':
    HANDLE = int(sys.argv[1])
    showPictures()

