# -*- coding: utf-8 -*-

from __future__ import print_function

import json
import requests

from .errors import PushbulletError

class Pushbullet(object):

    PUSH_URL = 'https://api.pushbullet.com/v2/pushes'

    def __init__(self, api_key):
        self.api_key = api_key

        self._session = requests.Session()
        self._session.auth = (self.api_key, '')
        self._session.headers.update({'Content-Type': 'application/json'})

    def push_note(self, title, body):
        data = {'type': 'note', 'title': title, 'body': body}

        return self._push(data)

    def push_link(self, title, url, body):
        data = {'type': 'link', 'title': title, 'url': url, 'body': body}

        return self._push(data)

    def _push(self, data):
        r = self._session.post(self.PUSH_URL, data=json.dumps(data))

        if r.status_code == requests.codes.ok:
            return r.json()
        else:
            raise PushbulletError(r.text)
