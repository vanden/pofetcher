import datetime

from subscription import Subscription

from config import NEWSDIR, WEEKDAYS, WEEKEND, ALLWEEK, M, T, W, TH, F, SA, SN

from renamer import TitleRenamer

HOUR = datetime.timedelta(seconds=60*60)
DEFAULTLAG = HOUR * 2

M, T, W, TH, F, S, SN = range(7)
SA = S
WEEKDAYS = [M, T, W, TH, F]

NewsSubscriptions = []

class NewsSubscription(Subscription):

    def __init__(self, *args, lag=DEFAULTLAG, **kwargs):
        self.lag = lag
        super().__init__(*args, **kwargs)

    def _shouldBeFetched(self, url):
        try:
            lastFetched = self.log[url]
        except KeyError:
            # Then, never yet fetch, so
            return True
        date, time = lastFetched.split('-')
        year, month, day = int(date[:4]), int(date[4:6]), int(date[6:])
        hour, minutes = int(time[:2]), int(time[2:])
        lastFetched = datetime.datetime(year, month, day, hour, minutes)
        now = datetime.datetime.now()
        return (now - lastFetched) > self.lag


cbchourlynews = NewsSubscription(
    feed="http://www.cbc.ca/podcasting/includes/hourlynews.xml",
    targetDir=NEWSDIR,
    count=1,
    renamer=TitleRenamer('CBCHourlyNews').rename,
    name='CBCHourlyNews',
    lag=HOUR,
)
NewsSubscriptions.append(cbchourlynews)

cbcworldatsix = NewsSubscription(
    feed="http://www.cbc.ca/podcasting/includes/w6.xml",
    targetDir=NEWSDIR,
    count=1,
    renamer=TitleRenamer('CBCWorldAtSix').rename,
    name='CBCWorldAtSix',
    days=WEEKDAYS
)

now = datetime.datetime.now()
if now.weekday() in WEEKDAYS:
    if now.hour >= 16 and now.hour <= 20:
        # FixMe This assumes I am in Pacific Time. Make it timezone aware
        NewsSubscriptions.append(cbcworldatsix)
