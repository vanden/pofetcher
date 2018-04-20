import datetime

class PodLog():

    def __init__(self, path):
        self.path = path
        self.lineLimit = (10**4)*2
        self.dataSplit = ' | '

        self._read()
        self._truncate()
        self._parse()


    def __contains__(self, url):
        return url in self.fetched_urls


    def _read(self):
        with open(self.path, 'r') as log:
            self.lines = [l for l in log.readlines() if l.strip()]


    def _truncate(self):
        if len(self.lines) > self.lineLimit:
            self.lines = self.lines[500:]
        self._write(self.lines)


    def _write(self, lines):
        with open(self.path, 'w') as log:
            log.write(''.join(lines))


    def _parse(self):
        self.fetched_urls = dict([line.split(self.dataSplit) for
                              line in self.lines])


    def update(self, url):
        # This isn't going to be the right thing once I move to forks or threads
        with open(self.path, 'a') as log:
            log.write(f"{url}{self.dataSplit}{self._timeStamp()}\n")


    def _timeStamp(self):
        return datetime.datetime.now().strftime("%Y%m%d-%H%M")
