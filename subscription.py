"""Provides a class for podcast subscriptions"""

import datetime
import os

import feedparser
import requests

from config import WEEKDAYS, WEEKEND, ALLWEEK, M, T, W, TH, F, SA, SN
from config import PODCASTDIR, PODLOG
from podlog import PodLog
from renamer import Renamer


THISDAY = datetime.datetime.now().weekday()

DEFAULTLOG = PodLog(PODLOG)

class Subscription():
    """Class for a podcast subscription

    The single public method fetchFeed parses the feed and attempts to
    download any new entries in the feed.

    The (goodly many) instance attributes are:

    feed:      the url of the podcast rss feed

    log:       the log file used to record what podcast files have
               already been downloaded on past runs

    targetDir: the directory in which the downloaded file should be save

    renamer:   a function to construct the local filename from the url
               and the entry (as produced by feedparser); typically this
               will be provided as a method of a subclass of Renamer

    name:      the name of the podcast; this is used in the on screen
               progress output

    days:      an iterable of day constants; if the current day is not
               in that iterable, the subscription is passed over. This
               allows for faster runs overall if it is know that a given
               podcast won't have new items today and is also a bit more
               polite.
    """
    def __init__(self, feed=None, log=None, targetDir=PODCASTDIR, count=5,
                 renamer=None, name=None, days=None):
        self.feed = feed
        self.log = log or DEFAULTLOG
        self.targetDir = targetDir
        self.count = count
        self.renamer = renamer or Renamer().rename
        self.name = name
        self.days = days or ALLWEEK

        # To prevent duplicate fetching which occurs with some feeds
        self.fetched = []


    def fetchFeed(self):
        """Parse the feed and attempts to fetch any podcasts it finds"""
        if THISDAY in self.days:
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

            if not self._shouldBeFetched(url):
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
                         f"{url} from {self.name}; skipping"]))

            print(f"\tFetching {url}")
            self._fetchAndWrite(url, entry)

    def _shouldBeFetched(self, url):
        # The basic one is making the assumption that all episodes in a feed
        # hav unique filenames and that a given episode may appear more than
        # once in a feed. The method exists so that subclasses may specialize
        # this behaviour.
        return not(url in self.log or url in self.fetched)

    def _fetchAndWrite(self, url, entry):
        localName = self._makeLocalName(url, entry)

        req = requests.get(url, stream=True)
        outfile = open(localName, 'wb')
        for chunk in req.iter_content(chunk_size=1024*4*4*4):
            if chunk:
                outfile.write(chunk)
        outfile.close()
        self.fetched.append(url)
        self.log.update(url)



    def _makeLocalName(self, url, entry):
        localName = os.path.join(self.targetDir,
                                 self.renamer(url, entry))
        while os.path.isfile(localName):
            localName = os.path.join(self.targetDir,
                                     self.renamer(url, entry))
        return localName
