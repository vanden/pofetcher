
class Renamer():

    def __init__(self, base=None):
        self.namesUsed = []
        self.base = base or ''


    def _clean(self, string):
        for (old, new) in [
                ('#',''), ('?',''), ('!', '_'), (' ','_'), ('%2C_', '_'),
                ('%2C', '_'), (':', '_'), ("'", ''), ('%2C', '_'),
                ('%2C', '_'), ('%2C', '_'), ('/', '_'), ('\\', '_'),
                ('*',''), ('"', ''), ("’", ''), ("“",""), ("”","")]:
            string = string.replace(old, new)

        return string


    def rename(self, url, entry, stamp):
        remoteFileName = url.rsplit('/', 1)[-1]
        self.remoteBase, self.remoteExt = remoteFileName.rsplit('.', 1)
        return self.makeCandidateName(url, entry, stamp)


    def makeCandidateName(self, url, entry, stamp):
        idn = 0
        while True:
            idn += 1
            candidate = self._clean(self._generateName(url, stamp, entry, idn))
            if candidate not in self.namesUsed:
                self.namesUsed.append(candidate)
                return candidate


    def _generateName(self, url, stamp, entry, idn):
        num = self._getIDNumerPart(idn)
        if self.base:
            if 'itunes_episode' in entry:
                candidate = f"{self.base}_{entry.itunes_episode}{num}.{self.remoteExt}"
            else:
                date = stamp.strftime("%Y%m%d")
                candidate = f"{self.base}_{date}{num}.{self.remoteExt}"
        else:
            candidate = f"{self.remoteBase}{num}.{self.remoteExt}"
        return candidate


    def _getIDNumerPart(self, idn):
        num=''
        if idn > 1:
            num = f"_{idn:03}"
        return num


    def _processHook(self, name):
        return name



class NullRenamer(Renamer):
    def _generateName(self, url, stamp, entry, idn):
        num = self._getIDNumerPart(idn)
        return f"{self.remoteBase}{num}.{self.remoteExt}"



class TitleITunesNumberRenamer(Renamer):
    def _generateName(self, url, stamp, entry, idn):
        num = self._getIDNumerPart(idn)
        return self._clean(
            f"{self.base}_{entry.itunes_episode}_{entry.title}_{num}.{self.remoteExt}")



class TitleRenamer(Renamer):
    def _generateName(self, url, stamp, entry, idn):

        num = self._getIDNumerPart(idn)
        if self.base:
            base = f"{self.base}_"
        else:
            base = ""
        name = f"{base}{entry.title}_{stamp}_{num}.{self.remoteExt}"
        name = self._processHook(name)
        return self._clean(name)
