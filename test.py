#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from pushbullet import Pushbullet

APIKEY = os.environ['APIKEY']

pb = Pushbullet(APIKEY)
pb.push_note('title', 'test push')
pb.push_link('title', 'https://example.com', 'test push')
