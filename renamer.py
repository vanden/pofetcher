
class Renamer():

    def __init__(self, base=None):
        self.namesUsed = []
        self.base = base


    def _clean(self, string):
        for (old, new) in [
                ('#',''), ('?',''), ('!', '_'), (' ','_'), ('%2C_', '_'),
                ('%2C', '_'), (':', '_'), ("'", ''), ('%2C', '_'),
                ('%2C', '_'), ('%2C', '_'), ('/', '_'), ('\\', '_'),
                ('*',''), ('"', ''), ("’", ''), ("“",""), ("”","")]:
            string = string.replace(old, new)
        
        return string

    def rename(self, url, entry, stamp):
        return self.makeCandidateName(url, entry, stamp)


    # I'm trying to make this fairly easy for subclasses to alter the naming
    # pattern. I'm not succeeding.
    def makeCandidateName(self, url, entry, stamp):
        remoteFileName = url.rsplit('/', 1)[-1]
        base, ext = remoteFileName.rsplit('.', 1)
        idn = 0
        while True:
            idn += 1
            candidate = self._clean(self._generateName(url, stamp, entry, idn))
            if candidate not in self.namesUsed:
                self.namesUsed.append(candidate)
                return candidate                

    def _generateName(self, url, stamp, entry, idn):
        # Duplication, but this lets the signature be simpler.
        remoteFileName = url.rsplit('/', 1)[-1]
        base, ext = remoteFileName.rsplit('.', 1)

        if idn > 1:
            num = self._getIDNumerPart(idn)
        else:
            num = ''
            
        if self.base:
            if 'itunes_episode' in entry:
                candidate = f"{self.base}_{entry.itunes_episode}{num}.{ext}"
            else:
                date = stamp.strftime("%Y%m%d")
                candidate = f"{self.base}_{date}{num}.{ext}"
        else:
            candidate = f"{base}{num}.{ext}"
        return candidate

    def _getIDNumerPart(self, idn): 
        num=''
        if idn > 1:
            num = f"_{idn:03}"
        return num

        
    

class NullRenamer(Renamer):
    def _generateName(self, url, stamp, entry, idn):
        remoteFileName = url.rsplit('/', 1)[-1]
        base, ext = remoteFileName.rsplit('.', 1)

        if idn > 1:
            num = f"_{idn:03}"
        else:
            num = ''

        return f"{base}{num}.{ext}"


class BaseTitleITunesNumberRenamer(Renamer):
    def _generateName(self, url, stamp, entry, idn):
        remoteFileName = url.rsplit('/', 1)[-1]
        base, ext = remoteFileName.rsplit('.', 1)
    
        if idn > 1:
            num = f"_{idn:03}"
        else:
            num = ''

        return self._clean(
            f"{self.base}_{entry.itunes_episode}_{entry.title}_{num}.{ext}")

class BBCRenamer(Renamer):
    def _generateName(self, url, stamp, entry, idn):
        remoteFileName = url.rsplit('/', 1)[-1]
        base, ext = remoteFileName.rsplit('.', 1)

        if idn > 1:
            num = f"_{idn:03}"
        else:
            num = ''

        return self._clean(
            f"BBC{self.base}_{stamp}{num}.{ext}")
        

class TitleRenamer(Renamer):
    def _generateName(self, url, stamp, entry, idn):
        remoteFileName = url.rsplit('/', 1)[-1]
        base, ext = remoteFileName.rsplit('.', 1)
        
        if idn > 1:
            num = f"_{idn:03}"
        else:
            num = ''
        if self.base:
            name = f"{self.base}_{entry.title}_{stamp}_{num}.{ext}"
        else:
            name = f"{entry.title}_{stamp}_{num}.{ext}"
        name = self._processHook(name)
        return self._clean(name)

    def _processHook(self, name):
        return name
