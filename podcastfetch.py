"""A simple script to manage the processing of podcast subscriptions"""

import cleaner

from subscriptions import subscriptions

for subscription in subscriptions:
    subscription.fetchFeed()
