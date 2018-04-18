import datetime, urllib.request, os
import feedparser, requests

podcastDir = '/home/brian/media/podcasts/podpad2'
podlog = os.path.join(podcastDir, 'podfetchlog')

from podlog import PodLog

class Subscription():

    def __init__(self, feed=None, log=None, targetDir=podcastDir, count=5,
                 renamer=None):
        self.feed = feed
        self.log = log
        self.targetDir = targetDir
        self.count = count
        self.renamer = renamer


    def parseFeed(self):
        feed = feedparser.parse(self.feed)
        entriesToFetch = []
        for entry in feed['entries'][:self.count]:
            if 'enclosures' in entry:
                entriesToFetch.append(entry)

        self._fetch(entriesToFetch)


    def _fetch(self, entries):
        for entry in entries:

            url = entry.enclosures[0].href
            if url in self.log:
                continue

            dts = None
            if 'published_parsed' in entry:
                dts = entry.published_parsed
            elif 'created_parsed' in entry:
                dts = entry.created_parsed
            if dts:
                stamp = datetime.datetime(dts.tm_year, dts.tm_mon,
                                          dts.tm_mday, dts.tm_hour,
                                          dts.tm_min, dts.tm_sec)
            else:
                stamp = datetime.datetime.now()

            localName = os.path.join(self.targetDir, self.renamer(url, stamp))
            print(url)
            if os.path.isfile(localName):
                # FixMe Do soemthing useful
                print("Seen already")
                continue

            r = requests.get(url)
            f = open(localName, 'wb')
            for chunk in r.iter_content(chunk_size = 1024*4*4*4):
                if chunk:
                    f.write(chunk)
            f.close()

            self.log.update(url)


class Renamer():
    def __init__(self, base):
        self.namesUsed = []

    def rename(self, url, pubdatetime):
        base = 'quirks'
        date = pubdatetime.strftime("%Y%m%d")
        idn = 1
        candidate = f"{base}_{date}_{idn:02}.mp3"
        while candidate in self.namesUsed:
            idn += 1
            candidate = f"{base}_{date}_{idn:02}.mp3"
        self.namesUsed.append(candidate)
        return candidate


log = PodLog(podlog)

subscriptions = []

quirks = Subscription(feed='http://www.cbc.ca/podcasting/includes/quirks.xml',
                      log=log,
                      targetDir='/home/brian/media/podcasts/podpad2/sci',
                      renamer = Renamer('quirks').rename,
                      count=10)
subscriptions.append(quirks)

for subscription in subscriptions:
    subscription.parseFeed()
