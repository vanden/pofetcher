from renamer import Renamer

from config import podlog
from podlog import PodLog
log = PodLog(podlog)


from subscription import Subscription

class Renamer():
    def __init__(self, base=None):
        self.namesUsed = []
        self.base = base

    def rename(self, url, pubdatetime):
        remoteFileName = url.rsplit('/', 1)[-1]
        date = pubdatetime.strftime("%Y%m%d")
        idn = 1

        candidate = f"{remoteFileName}"
        if self.base:
            candidate = f"{self.base}_{date}_{idn:02}.mp3"
        else:
            base, ext = remoteFileName.rsplit('.', 1)

        while candidate in self.namesUsed:
            idn += 1
            if self.base:
                candidate = f"{self.base}_{date}_{idn:02}.mp3"
            else:
                candidate = f"{base}_{idn:02}.{ext}"

        self.namesUsed.append(candidate)
        return candidate



subscriptions = []

quirks = Subscription(feed='http://www.cbc.ca/podcasting/includes/quirks.xml',
                      log=log,
                      targetDir='/home/brian/media/podcasts/podpad2/sci',
                      renamer = Renamer('quirks').rename,
                      count=10)
subscriptions.append(quirks)




