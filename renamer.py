"""Provides various classes for finding local names for downloaded
podcast files
"""

import datetime

class Renamer():
    """Class for determining the local name of a downloaded podcast file
    """
    def __init__(self, base=None):
        self.namesUsed = []
        self.base = base or ''


    def _clean(self, string):
        """Returns the string with unwanted characters replaced"""
        for (old, new) in [
                ('#', ''), ('?', ''), ('!', '_'), (' ', '_'), ('%2C_', '_'),
                ('%2C', '_'), (':', '_'), ("'", ''), ('%2C', '_'), (',', ''),
                ('%2C', '_'), ('%2C', '_'), ('/', '_'), ('\\', '_'), ('&', ''),
                ('*', ''), ('"', ''), ("’", ''), ("“", ""), ("”", "")]:
            string = string.replace(old, new)

        return string


    def _makeDateTimeStamp(self, entry):
        """returns a datetime.date drawn from entry data if possible"""
        dts = None
        if 'published_parsed' in entry:
            dts = entry.published_parsed
        elif 'created_parsed' in entry:
            dts = entry.created_parsed
        if dts:
            stamp = datetime.date(dts.tm_year, dts.tm_mon,
                                  dts.tm_mday)
        else:
            stamp = datetime.date.today()
        return stamp


    def rename(self, url, entry):
        """Produces the local filename to use"""
        stamp = self._makeDateTimeStamp(entry)
        remoteFileName = url.rsplit('/', 1)[-1]
        self.remoteBase, self.remoteExt = remoteFileName.rsplit('.', 1)
        return self.makeCandidateName(url, entry, stamp)


    def makeCandidateName(self, url, entry, stamp):
        """Badly named method; sort this out"""
        #Fixme
        idn = 0
        while True:
            idn += 1
            candidate = self._clean(self._generateName(url, stamp, entry, idn))
            candidate = self._processHook(candidate)
            if candidate not in self.namesUsed:
                self.namesUsed.append(candidate)
                return candidate


    def _generateName(self, url, stamp, entry, idn):
        # My best go at a default fallback name generator. But, given how much
        # some of the subclasses that provide a different implementation seem
        # to get, I'm not convinced I took a good guess at what would be the
        # most common case.
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
        # The intent is to have a distinct id number to prevent overwriting of
        # existing files. It doesn't seem too likely to be a problem, but I
        # have come across podcasts that helpfully use the same filename for
        # every episode.
        num = ''
        if idn > 1:
            num = f"_{idn:03}"
        return num


    def _processHook(self, name):
        # FixMe Bad name A hook method to allow a subclass to slightly tweak
        # the renaming behaviour of its parent.
        return name



class NullRenamer(Renamer):
    """Class for (nearly) null renaming.

    At most, it appends a unique number to the basename so as to enforce
    uniqueness.
    """
    def _generateName(self, url, stamp, entry, idn):
        num = self._getIDNumerPart(idn)
        return f"{self.remoteBase}{num}.{self.remoteExt}"



class TitleITunesNumberRenamer(Renamer):
    """
    Class for renaming using the itunes episode field of the rss entry
    """
    def _generateName(self, url, stamp, entry, idn):
        num = self._getIDNumerPart(idn)
        return self._clean(
            f"{self.base}_{entry.itunes_episode}_{entry.title}_{num}.{self.remoteExt}")



class TitleRenamer(Renamer):
    """Class for renaming by use of the title field of the rss entry"""
    def _generateName(self, url, stamp, entry, idn):

        num = self._getIDNumerPart(idn)
        if self.base:
            base = f"{self.base}_"
        else:
            base = ""
        name = f"{base}{stamp}_{entry.title}{num}.{self.remoteExt}"
        return self._clean(name)


class PostMp3StripTitleRenamer(TitleRenamer):
    """Class that adds stripping post extension characters from filename
    """
    def _processHook(self, name):
        front = name.split(".mp3")[0]
        return front + '.mp3'
