
from subscriptions import subscriptions
from config import podlog


for subscription in subscriptions:
    subscription.parseFeed()
