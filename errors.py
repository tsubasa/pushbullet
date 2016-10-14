# -*- coding: utf-8 -*-

from __future__ import print_function

import json

class PushbulletError(Exception):
    """Pushbullet exception"""

    def __init__(self, reason):
        self.reason = json.loads(reason)['error']['message']

    def __str__(self):
        return self.reason
