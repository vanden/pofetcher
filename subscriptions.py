from renamer import Renamer, NullRenamer, TitleITunesNumberRenamer
from renamer import TitleRenamer

from config import podlog
from podlog import PodLog
log = PodLog(podlog)


from subscription import Subscription


cbcSubscriptions = []
quirks = Subscription(
    feed='http://www.cbc.ca/podcasting/includes/quirks.xml',
    targetDir='/home/brian/media/podcasts/podpad2/sci',
    renamer = Renamer('quirks').rename,
    count=10,
    name="Quirks & Quarks"
)


atissue = Subscription(
    feed='http://www.cbc.ca/podcasting/includes/atissue.xml',
    targetDir='/home/brian/media/podcasts/podpad2/news',
    renamer = Renamer('AtIssue').rename,
    count=3,
    name="At Issue"
)


otherpeoplesproblems = Subscription(
    feed='http://www.cbc.ca/podcasting/includes/opp.xml',
    targetDir='/home/brian/media/podcasts/podpad2/cbc',
    renamer = TitleRenamer('CBCOtherPeoplesProblems').rename,
    count=2,
    name="Other Peoples Problems"
)


ondrugs = Subscription(
    feed='http://www.cbc.ca/podcasting/includes/ondrugs.xml',
    targetDir='/home/brian/media/podcasts/podpad2/cbc',
    renamer = TitleRenamer('CBCOnDrugs').rename,
    count=3,
    name="On Drugs"
)


whitecoat = Subscription(
    feed='http://www.cbc.ca/podcasting/includes/whitecoat.xml',
    targetDir='/home/brian/media/podcasts/podpad2/cbc',
    renamer = TitleRenamer('CBCWhiteCoatBlackArt').rename,
    count=3,
    name="White Coat Black Art"
)


spark = Subscription(
    feed='http://www.cbc.ca/podcasting/includes/spark.xml',
    targetDir='/home/brian/media/podcasts/podpad2/cbc',
    renamer = TitleRenamer('CBCSpark').rename,
    count=3,
    name="Spark"
)



undertheinfluence = Subscription(
    feed='http://www.cbc.ca/podcasting/includes/undertheinfluence.xml',
    targetDir='/home/brian/media/podcasts/podpad2/cbc',
    renamer = TitleRenamer('CBCUnderTheInfluence').rename,
    count=2,
    name="Under The Influence"
)


cbcSubscriptions = [
    quirks,
    atissue,
    otherpeoplesproblems,
    ondrugs,
    spark,
    whitecoat,
    undertheinfluence,
]




gotime = Subscription(
    feed='https://changelog.com/gotime/feed',
    targetDir='/home/brian/media/podcasts/podpad2/prog',
    count=8,
    name="GoTime",
)


hanselMinutes = Subscription(
    feed='https://rss.simplecast.com/podcasts/4669/rss',
    targetDir='/home/brian/media/podcasts/podpad2/prog',
    count=8,
    renamer = TitleRenamer('hansleminutes').rename,
    name = "HanselMinutes",
)


syntax = Subscription(
    feed='http://feed.syntax.fm/rss',
    targetDir='/home/brian/media/podcasts/podpad2/prog',
    count=3,
    renamer = NullRenamer().rename,
    name = "Syntax"
)


javascriptjabber = Subscription(
    feed='https://feeds.feedwrench.com/JavaScriptJabber.rss',
    targetDir='/home/brian/media/podcasts/podpad2/prog',
    count=5,
    renamer = NullRenamer().rename,
    name = "JavaScriptJabber"
)

podcastinit = Subscription(
    feed='https://www.podcastinit.com/feed/mp3/',
    targetDir='/home/brian/media/podcasts/podpad2/prog',
    count=10,
    renamer = TitleRenamer('Podcast.__init__').rename,
    name = "Podcast.__init__"
)


testandcode = Subscription(
    feed='http://testandcode.com/rss/',
    targetDir='/home/brian/media/podcasts/podpad2/prog',
    count=2,
    renamer = TitleRenamer('TestAndCode').rename,
    name = "TestAndCode"
)





# What's this, then? Got both.
# Parsing JavaScriptJabber
# 	Fetching https://media.devchat.tv/js-jabber/JSJ_309_WebAssembly_and_JavaScript_with_Ben_Titzer.mp3
# 	Fetching https://media.devchat.tv/js-jabber/JSJ_309_WebAssembly_and_JavaScript_with_Ben_Titzer.mp3


talkpythontome = Subscription(
    feed='https://talkpython.fm/episodes/ogg_rss',
    targetDir='/home/brian/media/podcasts/podpad2/prog',
    count=5,
    renamer = TitleITunesNumberRenamer("TalkPythonToMe").rename,
    name = "TalkPythonToMe"
)


importthis = Subscription(
    feed='http://feeds.soundcloud.com/users/soundcloud:users:82237854/sounds.rss',
    targetDir='/home/brian/media/podcasts/podpad2/prog',
    count=10,
    renamer = TitleRenamer("ImportThis").rename,
    name = "ImportThis"
)



fullstackradio = Subscription(
    feed='https://rss.simplecast.com/podcasts/279/rss',
    targetDir='/home/brian/media/podcasts/podpad2/prog',
    count=10,
    renamer = TitleRenamer("FullStackRadio").rename,
    name = "FullStackRadio"
)


thechangelog = Subscription(
    feed='https://changelog.com/podcast/feed',
    targetDir='/home/brian/media/podcasts/podpad2/prog',
    count=10,
    renamer = TitleRenamer("TheChangeLog").rename,
    name = "TheChangeLog"
)



programmingSubscriptions = [
    thechangelog,
    podcastinit,
    talkpythontome,
    hanselMinutes,
    gotime,
    fullstackradio,
    syntax,
    testandcode,
    javascriptjabber,
    importthis
]


bbcanalysis = Subscription(
    feed='http://www.bbc.co.uk/programmes/b006r4vz/episodes/downloads.rss',
    targetDir='/home/brian/media/podcasts/podpad2/bbc',
    count=2,
    renamer = TitleRenamer("BBCAnalysis").rename,
    name = "BBCAnalysis"
)


bbceverydayethics = Subscription(
    feed='http://www.bbc.co.uk/programmes/p02nrsmh/episodes/downloads.rss',
    targetDir='/home/brian/media/podcasts/podpad2/bbc',
    count=1,
    renamer = TitleRenamer("BBCEveryDayEthics").rename,
    name = "BBCEveryDayEthics"
)

bbclifescientific = Subscription(
    feed="http://www.bbc.co.uk/programmes/b015sqc7/episodes/downloads.rss",
    targetDir='/home/brian/media/podcasts/podpad2/sci',
    count=1,
    renamer = TitleRenamer("BBCLifeScientific").rename,
    name = "BBCLifeScientific"
)


bbcipm = Subscription(
    feed='http://www.bbc.co.uk/programmes/p02nrtwc/episodes/downloads.rss',
    targetDir='/home/brian/media/podcasts/podpad2/bbc',
    count=1,
    renamer = TitleRenamer("BBCiPM").rename,
    name = "BBCiPM"
)


bbcdiscovery =  Subscription(
    feed='https://podcasts.files.bbci.co.uk/p002w557.rss',
    targetDir='/home/brian/media/podcasts/podpad2/sci',
    count=1,
    renamer = TitleRenamer("BBCDiscovery").rename,
    name = "BBCDiscovery"
)



bbcwitness = Subscription(
    feed='http://www.bbc.co.uk/programmes/p004t1hd/episodes/downloads.rss',
    targetDir='/home/brian/media/podcasts/podpad2/bbc',
    count=7,
    renamer = TitleRenamer("BBCWitness").rename,
    name = "BBCWitness"
)


bbcdrkarl = Subscription(
    feed='https://podcasts.files.bbci.co.uk/p02pc9ny.rss',
    targetDir='/home/brian/media/podcasts/podpad2/sci',
    count=3,
    # Leaving it as title to see if it distinguishes dr karl from non
    renamer = TitleRenamer("BBCDrKarl").rename,
    name = "BBCDrKarl"
)


bbcclick = Subscription(
    feed='http://www.bbc.co.uk/programmes/p002w6r2/episodes/downloads.rss',
    targetDir='/home/brian/media/podcasts/podpad2/geek',
    count=1,
    renamer = TitleRenamer("BBCClick").rename,
    name = "BBCClick"
)


bbceddiemair = Subscription(
    feed='http://www.bbc.co.uk/programmes/p03m4q5s/episodes/downloads.rss',
    targetDir='/home/brian/media/podcasts/podpad2/bbc',
    count=1,
    renamer = TitleRenamer("BBCEddieMair").rename,
    name = "BBCEddieMair"
)


bbctechtent = Subscription(
    feed='http://www.bbc.co.uk/programmes/p01plr2p/episodes/downloads.rss',
    targetDir='/home/brian/media/podcasts/podpad2/geek',
    count=1,
    renamer = TitleRenamer("BBCTechTent").rename,
    name = "BBCTechTent"
)


bbcfileonfour =  Subscription(
    feed='https://podcasts.files.bbci.co.uk/b006th08.rss',
    targetDir='/home/brian/media/podcasts/podpad2/bbc',
    count=4,
    renamer = TitleRenamer("BBCFileOnFour").rename,
    name = "BBCFileOnFour"
)


bbcscienceinaction = Subscription(
    feed='http://www.bbc.co.uk/programmes/p002vsnb/episodes/downloads.rss',
    targetDir='/home/brian/media/podcasts/podpad2/sci',
    count=1,
    renamer = Renamer("BBCScienceInAction").rename,
    name = "BBCScienceInAction"
)


bbcgreatlives = Subscription(
    feed='http://www.bbc.co.uk/programmes/b006qxsb/episodes/downloads.rss',
    targetDir='/home/brian/media/podcasts/podpad2/bbc',
    count=2,
    renamer = TitleRenamer("BBCGreatLives").rename,
    name = "BBCGreatLives"
)




bbcinourtime = Subscription(
    feed='http://www.bbc.co.uk/programmes/b006qykl/episodes/downloads.rss',
    targetDir='/home/brian/media/podcasts/podpad2/bbc',
    count=1,
    renamer = TitleRenamer("BBCInOurTime").rename,
    name = "BBCInOurTime"
)





bbcmoralmaze = Subscription(
    feed='http://www.bbc.co.uk/programmes/b006qk11/episodes/downloads.rss',
    targetDir='/home/brian/media/podcasts/podpad2/bbc',
    count=1,
    renamer = TitleRenamer("BBCMoralMaze").rename,
    name = "BBCMoralMaze"
)



bbcr4report = Subscription(
    feed='http://www.bbc.co.uk/programmes/b00jkr1q/episodes/downloads.rss',
    targetDir='/home/brian/media/podcasts/podpad2/bbc',
    count=1,
    renamer = TitleRenamer("BBCR4Report").rename,
    name = "BBCR4Report"
)


bbcinsidescience = Subscription(
    feed='http://www.bbc.co.uk/programmes/b036f7w2/episodes/downloads.rss',
    targetDir='/home/brian/media/podcasts/podpad2/sci',
    count=1,
    renamer = TitleRenamer("BBCInsideScience").rename,
    name = "BBCInsideScience"
)



bbcSubscriptions = [
    bbceverydayethics,
    bbcipm,
    bbcmoralmaze,
    bbcfileonfour,
    bbcinourtime,
    bbcr4report,
    bbcanalysis,
    bbcwitness,
    bbcgreatlives,
    bbceddiemair,
]



thePenAddict = Subscription(
    feed='https://www.relay.fm/penaddict/feed',
    targetDir='/home/brian/media/podcasts/podpad2/pens',
    count=2,
    renamer = NullRenamer().rename,
    name = "The Pen Addict"
)


goulet = Subscription(
    feed='http://feeds.feedburner.com/GouletQa',
    targetDir='/home/brian/media/podcasts/podpad2/pens',
    count=2,
    renamer = NullRenamer().rename,
    name = "Goulet"
)




class tenPerRenamer(Renamer):
    def _generateName(self, url, stamp, entry, idn):
        number = entry.title.split(':')[0].strip('#')
        num = self._getIDNumerPart(idn)
        return f"10PercentHappier_{number}{num}.mp3"

tenpercenthappier = Subscription(
    feed='http://feeds.feedburner.com/abcradio/10percenthappier?format=xml',
    targetDir='/home/brian/media/podcasts/podpad2/buddhist',
    count=2,
    renamer = tenPerRenamer().rename,
    name = "Ten Percent Happier"
)


ninety9percentinvisible = Subscription(
    feed='http://feeds.99percentinvisible.org/99percentinvisible',
    targetDir='/home/brian/media/podcasts/podpad2/geek',
    count=10,
    renamer = Renamer('99PercentInvisible').rename,
    name = "99 Percent Invisible"
)

class SciAmRenamer(TitleRenamer):
    def _processHook(self, name):
        front = name.split(".mp3")[0]
        return front + '.mp3'


allinthemind = Subscription(
    feed='http://www.abc.net.au/radionational/feed/2888650/podcast.xml',
    targetDir='/home/brian/media/podcasts/podpad2/sci',
    count=2,
    renamer = TitleRenamer("AllInTheMind").rename,
    name = "AllInTheMind"
)


ockhamsrazor = Subscription(
    feed='http://www.abc.net.au/radionational/feed/2883682/podcast.xml',
    targetDir='/home/brian/media/podcasts/podpad2/sci',
    count=2,
    renamer = TitleRenamer("OckhamsRazor").rename,
    name = "OckhamsRazor"
)


sixtysecondscience = Subscription(
    feed='http://rss.sciam.com/sciam/60secsciencepodcast?format=xml',
    targetDir='/home/brian/media/podcasts/podpad2/sci',
    count=20,
    renamer = SciAmRenamer("SixtySecondScience").rename,
    name = "SixtySecondScience"
)


greatmomentsinscience = Subscription(
    feed='http://www.abc.net.au/radionational/feed/7417248/podcast.xml',
    targetDir='/home/brian/media/podcasts/podpad2/sci',
    count=108,
    renamer = TitleRenamer("GreatMomentsInScience").rename,
    name = "GreatMomentsInScience"
)


thescienceshow = Subscription(
    feed='http://www.abc.net.au/radionational/feed/2885486/podcast.xml',
    targetDir='/home/brian/media/podcasts/podpad2/sci',
    count=20,
    renamer = TitleRenamer("TheScienceShow").rename,
    name = "TheScienceShow"
)


spacetime = Subscription(
    feed='https://audioboom.com/channels/4642443.rss',
    targetDir='/home/brian/media/podcasts/podpad2/sci',
    count=2,
    renamer = TitleRenamer("SpaceTime").rename,
    name = "SpaceTime"
)



enginesofingenuity = Subscription(
    feed='https://www.houstonpublicmedia.org/podcasts/engines-of-our-ingenuity/',
    targetDir='/home/brian/media/podcasts/podpad2/sci',
    count=30,
    renamer = TitleRenamer().rename,
    name = "Engines Of Our Ingenuity"
)


sciencepodcasts = [
    sixtysecondscience,
    greatmomentsinscience,
    bbclifescientific,
    bbcinsidescience,
    bbcdrkarl,
    bbcdiscovery,
    bbcscienceinaction,
    thescienceshow,
    allinthemind,
    ockhamsrazor
]


heresthething = Subscription(
    feed='http://feeds.wnyc.org/wnycheresthething',
    targetDir='/home/brian/media/podcasts/podpad2/geek',
    count=3,
    renamer = TitleRenamer('HeresTheThing').rename,
    name = "HeresTheThing"
)



downloadthisshow = Subscription(
    feed='http://www.abc.net.au/radionational/feed/3777916/podcast.xml',
    targetDir='/home/brian/media/podcasts/podpad2/geek',
    count=2,
    renamer = TitleRenamer('DownloadThisShow').rename,
    name = "DownloadThisShow"
)


futuretense = Subscription(
    feed='http://www.abc.net.au/radionational/feed/2883726/podcast.xml',
    targetDir='/home/brian/media/podcasts/podpad2/geek',
    count=2,
    renamer = TitleRenamer('FutureTense').rename,
    name = "FutureTense"
)



thephilosopherszone = Subscription(
    feed='http://www.abc.net.au/radionational/feed/2884506/podcast.xml',
    targetDir='/home/brian/media/podcasts/podpad2/geek',
    count=1,
    renamer = TitleRenamer('ThePhilosophersZone').rename,
    name = "ThePhilosophersZone"
)

beyondthetodolist = Subscription(
    feed="http://feeds2.noodle.mx/beyondthetodolist",
    targetDir='/home/brian/media/podcasts/podpad2/geek',
    count=1,
    renamer = TitleRenamer('BeyondTheToDoList').rename,
    name = "BeyondTheToDoList"
)


geekSubscriptions = [
    beyondthetodolist,
    bbcclick,
    bbctechtent,
    heresthething,
    downloadthisshow,
    goulet,
    thePenAddict,
    tenpercenthappier,
    ninety9percentinvisible,
    enginesofingenuity,
    futuretense,
    thephilosopherszone
]





ubunutuuk = Subscription(
    feed="http://ubuntupodcast.org/feed/podcast",
    targetDir='/home/brian/media/podcasts/podpad2/linux',
    count=1,
    renamer = TitleRenamer('UbuntuUK').rename,
    name = "UbuntuUK"
)



linuxvoice = Subscription(
    feed = "http://www.linuxvoice.com/podcast_ogg.rss",
    targetDir='/home/brian/media/podcasts/podpad2/linux',
    count=1,
    renamer = TitleRenamer('LinuxVoice').rename,
    name = "LinuxVoice"
)

flossweekly = Subscription(
    feed="http://feeds.twit.tv/floss.xml",
    targetDir='/home/brian/media/podcasts/podpad2/linux',
    count=1,
    renamer = NullRenamer().rename,
    name = "FLOSSWeekly"
)



linuxSubscriptions = [
    linuxvoice,
    ubunutuuk,
    flossweekly,
]



subscriptions = []
for sub in [
        bbcSubscriptions,
        cbcSubscriptions,
        sciencepodcasts,
        programmingSubscriptions,
        geekSubscriptions,
        linuxSubscriptions,
        ]:
    subscriptions.extend(sub)

