#
# This file is part of Flask-Notifications
# Copyright (C) 2015 CERN.
#
# Flask-Notifications is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

from sse import Sse


class SseNotifier(object):
    def __init__(self, pubsub, channel):
        self.pubsub = pubsub
        self.pubsub.subscribe(channel)
        self.sse = Sse()

    def __iter__(self):
        for message in self.pubsub.listen():
            if message['type'] == 'message':
                print(str(message))
                self.sse.add_message("", message['data'])
                for data in self.sse:
                    yield data.encode('u8')
