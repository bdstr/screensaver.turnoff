# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Dag Wieers (@dagwieers) <dag@wieers.com>
# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
''' This file implements the Kodi xbmc module, either using stubs or alternative functionality '''

# pylint: disable=invalid-name,no-self-use,unused-argument

from __future__ import absolute_import, division, print_function, unicode_literals

import os
import json
import time
from xbmcextra import ADDON_ID, global_settings, import_language


LOGLEVELS = ['Debug', 'Info', 'Notice', 'Warning', 'Error', 'Severe', 'Fatal', 'None']
LOGDEBUG = 0
LOGINFO = 1
LOGNOTICE = 2
LOGWARNING = 3
LOGERROR = 4
LOGSEVERE = 5
LOGFATAL = 6
LOGNONE = 7

INFO_LABELS = {
    'Container.FolderPath': 'plugin://' + ADDON_ID + '/',
    'System.BuildVersion': '18.2',
}

REGIONS = {
    'datelong': '%A, %e %B %Y',
    'dateshort': '%Y-%m-%d',
}

settings = global_settings()


class Keyboard(object):
    ''' A stub implementation of the xbmc Keyboard class '''

    def __init__(self, line='', heading=''):
        ''' A stub constructor for the xbmc Keyboard class '''

    def doModal(self, autoclose=0):
        ''' A stub implementation for the xbmc Keyboard class doModal() method '''

    def isConfirmed(self):
        ''' A stub implementation for the xbmc Keyboard class isConfirmed() method '''
        return True

    def getText(self):
        ''' A stub implementation for the xbmc Keyboard class getText() method '''
        return 'test'


class Monitor(object):
    ''' A stub implementation of the xbmc Monitor class '''

    def __init__(self, line='', heading=''):
        ''' A stub constructor for the xbmc Monitor class '''
        self.iteration = 0

    def abortRequested(self):
        ''' A stub implementation for the xbmc Monitor class abortRequested() method '''
        self.iteration += 1
        print('Iteration: %s' % self.iteration)
        return self.iteration % 5 == 0

    def waitForAbort(self, timeout=None):
        ''' A stub implementation for the xbmc Monitor class waitForAbort() method '''
        try:
            time.sleep(timeout)
        except KeyboardInterrupt:
            return True
        except Exception:  # pylint: disable=broad-except
            return True
        return False


class Player(object):
    ''' A stub implementation of the xbmc Player class '''
    def __init__(self):
        ''' A stub constructor for the xbmc Player class '''
        self._count = 0

    def play(self, item='', listitem=None, windowed=False, startpos=-1):
        ''' A stub implementation for the xbmc Player class play() method '''
        return

    def stop(self):
        ''' A stub implementation for the xbmc Player class stop() method '''
        return

    def getPlayingFile(self):
        ''' A stub implementation for the xbmc Player class getPlayingFile() method '''
        return '/foo/bar'

    def isPlaying(self):
        ''' A stub implementation for the xbmc Player class isPlaying() method '''
        # Return True four times out of five
        self._count += 1
        return bool(self._count % 5 != 0)

    def seekTime(self, seekTime):
        ''' A stub implementation for the xbmc Player class seekTime() method '''
        return

    def showSubtitles(self, bVisible):
        ''' A stub implementation for the xbmc Player class showSubtitles() method '''
        return

    def getTotalTime(self):
        ''' A stub implementation for the xbmc Player class getTotalTime() method '''
        return 0

    def getTime(self):
        ''' A stub implementation for the xbmc Player class getTime() method '''
        return 0

    def getVideoInfoTag(self):
        ''' A stub implementation for the xbmc Player class getVideoInfoTag() method '''
        return VideoInfoTag()


class PlayList(object):
    ''' A stub implementation of the xbmc PlayList class '''

    def __init__(self):
        ''' A stub constructor for the xbmc PlayList class '''

    def getposition(self):
        ''' A stub implementation for the xbmc PlayList class getposition() method '''
        return 0

    def size(self):
        ''' A stub implementation for the xbmc PlayList class size() method '''


class VideoInfoTag(object):
    ''' A stub implementation of the xbmc VideoInfoTag class '''

    def __init__(self):
        ''' A stub constructor for the xbmc VideoInfoTag class '''

    def getSeason(self):
        ''' A stub implementation for the xbmc VideoInfoTag class getSeason() method '''
        return 0

    def getEpisode(self):
        ''' A stub implementation for the xbmc VideoInfoTag class getEpisode() method '''
        return 0

    def getTVShowTitle(self):
        ''' A stub implementation for the xbmc VideoInfoTag class getTVShowTitle() method '''
        return ''

    def getPlayCount(self):
        ''' A stub implementation for the xbmc VideoInfoTag class getPlayCount() method '''
        return 0

    def getRating(self):
        ''' A stub implementation for the xbmc VideoInfoTag class getRating() method '''
        return 0


def executebuiltin(string, wait=False):  # pylint: disable=unused-argument
    ''' A stub implementation of the xbmc executebuiltin() function '''
    return


def executeJSONRPC(jsonrpccommand):
    ''' A reimplementation of the xbmc executeJSONRPC() function '''
    command = json.loads(jsonrpccommand)
    if command.get('method') == 'Settings.GetSettingValue':
        key = command.get('params').get('setting')
        return json.dumps(dict(id=1, jsonrpc='2.0', result=dict(value=settings.get(key))))
    if command.get('method') == 'Addons.GetAddonDetails':
        if command.get('params', {}).get('addonid') == 'script.module.inputstreamhelper':
            return json.dumps(dict(id=1, jsonrpc='2.0', result=dict(addon=dict(enabled='true', version='0.3.5'))))
        return json.dumps(dict(id=1, jsonrpc='2.0', result=dict(addon=dict(enabled='true', version='1.2.3'))))
    if command.get('method') == 'Textures.GetTextures':
        return json.dumps(dict(id=1, jsonrpc='2.0', result=dict(textures=[dict(cachedurl="", imagehash="", lasthashcheck="", textureid=4837, url="")])))
    if command.get('method') == 'Textures.RemoveTexture':
        return json.dumps(dict(id=1, jsonrpc='2.0', result="OK"))
    log("executeJSONRPC does not implement method '{method}'".format(**command), LOGERROR)
    return json.dumps(dict(error=dict(code=-1, message='Not implemented'), id=1, jsonrpc='2.0'))


def getCondVisibility(string):  # pylint: disable=unused-argument
    ''' A reimplementation of the xbmc getCondVisibility() function '''
    if string == 'system.platform.android':
        return False
    if string.startswith('System.HasAddon'):
        return True
    return True


def getInfoLabel(key):
    ''' A reimplementation of the xbmc getInfoLabel() function '''
    return INFO_LABELS.get(key)


def getLocalizedString(msgctxt):
    ''' A reimplementation of the xbmc getLocalizedString() function '''
    for entry in import_language(language=settings.get('locale.language')):
        if entry.msgctxt == '#%s' % msgctxt:
            return entry.msgstr or entry.msgid
    if int(msgctxt) >= 30000:
        log('Unable to translate #{msgctxt}'.format(msgctxt=msgctxt), LOGERROR)
    return '<Untranslated>'


def getRegion(key):
    ''' A reimplementation of the xbmc getRegion() function '''
    return REGIONS.get(key)


def log(msg, level=0):
    ''' A reimplementation of the xbmc log() function '''
    color1 = '\033[32;1m'
    color2 = '\033[32;0m'
    name = LOGLEVELS[level]
    if level in (4, 5, 6, 7):
        color1 = '\033[31;1m'
        if level in (6, 7):
            raise Exception(msg)
    elif level in (2, 3):
        color1 = '\033[33;1m'
    elif level == 0:
        color2 = '\033[30;1m'
    print('{color1}{name}: {color2}{msg}\033[39;0m'.format(name=name, color1=color1, color2=color2, msg=msg))


def setContent(self, content):
    ''' A stub implementation of the xbmc setContent() function '''
    return


def sleep(timemillis):
    ''' A reimplementation of the xbmc sleep() function '''
    time.sleep(timemillis / 1000)


def translatePath(path):
    ''' A stub implementation of the xbmc translatePath() function '''
    if path.startswith('special://home'):
        return path.replace('special://home', os.path.join(os.getcwd(), 'test/'))
    if path.startswith('special://masterprofile'):
        return path.replace('special://masterprofile', os.path.join(os.getcwd(), 'test/userdata/'))
    if path.startswith('special://profile'):
        return path.replace('special://profile', os.path.join(os.getcwd(), 'test/userdata/'))
    if path.startswith('special://userdata'):
        return path.replace('special://userdata', os.path.join(os.getcwd(), 'test/userdata/'))
    return path
