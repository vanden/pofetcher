
from subscriptions import subscriptions
from config import podlog

# from podlog import PodLog
# log = PodLog(podlog)



for subscription in subscriptions:
    subscription.parseFeed()
