# -*- coding: utf-8 -*-

import json

class PushbulletError(Exception):
    """Pushbullet exception"""

    def __init__(self, reason):
        self.reason = json.loads(reason)['error']['message']

    def __str__(self):
        return self.reason
