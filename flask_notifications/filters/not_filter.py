#
# This file is part of Flask-Notifications
# Copyright (C) 2015 CERN.
#
# Flask-Notifications is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

from flask_notifications.event_filter import EventFilter


class Not(EventFilter):

    def __init__(self, event_filter):
        self.event_filter = event_filter

    def filter(self, event, *args, **kwargs):
        return not self.event_filter(event)
