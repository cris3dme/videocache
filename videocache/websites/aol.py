#!/usr/bin/env python
#
# (C) Copyright 2008-2011 White Magnet Software Pvt Ltd.
#
# For more information check http://cachevideos.com/
#

__author__ = """Kulbir Saini <saini@saini.co.in>"""
__docformat__ = 'plaintext'

import re

def check_aol_video(host, path, query, url):
    matched, website_id, video_id, format, search, queue = True, 'aol', None, '', True, True

    if host.find('stream.aol.com') > -1 and re.compile('(.*)/[a-zA-Z0-9]+\/(.*)\.(flv)').search(path) and (path.find('.flv') > -1 or path.find('.mp4') > -1):
        try:
            video_id = '_'.join(path.strip('/').split('/')[-2:])
        except Exception, e:
            pass
    else:
        matched = False

    return (matched, website_id, video_id, format, search, queue)
