"""A simple script to manage the processing of podcast subscriptions"""

from subscriptions import subscriptions

for subscription in subscriptions:
    subscription.fetchFeed()
