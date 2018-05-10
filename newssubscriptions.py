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
            # Then never yet fetched, so
            return True
        date, time = lastFetched.split('-')
        year, month, day = int(date[:4]), int(date[4:6]), int(date[6:])
        hour, minutes = int(time[:2]), int(time[2:])
        lastFetched = datetime.datetime(year, month, day, hour, minutes)
        return (datetime.datetime.now() - lastFetched) > self.lag



bbcworldthisweek = Subscription(
    feed="http://www.bbc.co.uk/programmes/p0299wgd/episodes/downloads.rss",
    targetDir=NEWSDIR,
    count=1,
    renamer=TitleRenamer('BBCWorldThisWeek').rename,
    name="BBCWorldThisWeek",
    days=WEEKEND
)


cbchourlynews = NewsSubscription(
    feed="http://www.cbc.ca/podcasting/includes/hourlynews.xml",
    targetDir=NEWSDIR,
    count=1,
    renamer=TitleRenamer('CBCHourlyNews').rename,
    name='CBCHourlyNews',
    lag=HOUR,
)
NewsSubscriptions.append(cbchourlynews)


bbcnewshour = NewsSubscription(
    feed="http://podcasts.files.bbci.co.uk/p002vsnk.rss",
    targetDir=NEWSDIR,
    count=1,
    renamer=TitleRenamer('BBCNewsHour').rename,
    name="BBCNewsHour",
    lag=HOUR*4
)
NewsSubscriptions.append(bbcnewshour)



cbcworldreport = NewsSubscription(
    feed="http://www.cbc.ca/podcasting/includes/wr.xml",
    targetDir=NEWSDIR,
    count=1,
    renamer=TitleRenamer('CBCWorldReport').rename,
    name="CBCWorldReport",
    lag=HOUR*8
)


cbcworldatsix = NewsSubscription(
    feed="http://www.cbc.ca/podcasting/includes/w6.xml",
    targetDir=NEWSDIR,
    count=1,
    renamer=TitleRenamer('CBCWorldAtSix').rename,
    name='CBCWorldAtSix',
    days=WEEKDAYS,
    lag=HOUR*14
)

now = datetime.datetime.now()
if now.weekday() in WEEKDAYS:
    if now.hour >= 16 and now.hour <= 23:
        # FixMe This assumes I am in Pacific Time. Make it timezone aware
        NewsSubscriptions.append(cbcworldatsix)

if now.hour >= 7 and now.hour <= 12:
    NewsSubscriptions.insert(0, cbcworldreport)

if now.weekday() in WEEKEND:
    NewsSubscriptions.append(bbcworldthisweek)
