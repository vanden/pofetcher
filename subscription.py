import datetime, os

import feedparser, requests

from config import podcastDir, podlog
from renamer import Renamer


class Subscription():

    def __init__(self, feed=None, log=None, targetDir=podcastDir, count=5,
                 renamer=None, name=None):
        self.feed = feed
        self.log = log
        self.targetDir = targetDir
        self.count = count
        self.renamer = renamer or Renamer().rename
        self.name = name

        # To prevent duplicate fetching which occurs with some feeds
        self.fetched = []


    def parseFeed(self):
        print(f"Parsing {self.name}")
        feed = feedparser.parse(self.feed)
        entriesToFetch = []
        for entry in feed['entries'][:self.count]:
            if 'enclosures' in entry:
                entriesToFetch.append(entry)

        self._fetch(entriesToFetch)


    def _fetch(self, entries):
        for entry in entries:
            try:
                url = entry.enclosures[0].href
            except IndexError:
                # It seems that this can occur when a podcast feed includes
                # non-podcast items, too. Not sure what more if anything I
                # should do. ThinkMore
                continue

            if url in self.log or url in self.fetched:
                continue

            if '?' in url:
                # Some feeds have a '?' after the file extension leading off
                # some metadata. Pull that all off to see if the file format
                # is one we want.
                realurl = url.split('?', 1)[0]
                if not realurl.split('.')[-1] in ['mp3', 'ogg']:
                    print(''.join(
                        # FixMe Isn't really the issue, is it?
                        ["Don't know how to parse",
                         f"{orig_url} from {self.name}; skipping"]))

            print(f"\tFetching {url}")
            self._fetchAndWrite(url, entry)


    def _fetchAndWrite(self, url, entry):
        localName = self._makeLocalName(url, entry)

        r = requests.get(url, stream=True)
        f = open(localName, 'wb')
        for chunk in r.iter_content(chunk_size = 1024*4*4*4):
            if chunk:
                f.write(chunk)
        f.close()
        self.fetched.append(url)
        self.log.update(url)


    def _makeDateTimeStamp(self, entry):
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
        return stamp


    def _makeLocalName(self, url, entry):
        stamp = self._makeDateTimeStamp(entry)
        localName = os.path.join(self.targetDir,
                                 self.renamer(url, entry, stamp))
        while os.path.isfile(localName):
            localName = os.path.join(self.targetDir,
                                     self.renamer(url, entry, stamp))
        return localName
