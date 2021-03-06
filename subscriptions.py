import os

from renamer import Renamer, NullRenamer, TitleITunesNumberRenamer
from renamer import TitleRenamer, PostMp3StripTitleRenamer

from subscription import Subscription
from config import WEEKDAYS, WEEKEND, ALLWEEK, M, T, W, TH, F, SA, SN

from config import PODLOG
from config import PODCASTDIR
from config import NEWSDIR
from podlog import PodLog


from newssubscriptions import NewsSubscriptions

log = PodLog(PODLOG)



bbcDir = os.path.join(PODCASTDIR, 'bbc')
cbcDir = os.path.join(PODCASTDIR, 'cbc')
geekDir = os.path.join(PODCASTDIR, 'geek')
linuxDir = os.path.join(PODCASTDIR, 'linux')
penDir = os.path.join(PODCASTDIR, 'pens')
philDir = os.path.join(PODCASTDIR, 'phil')
programmingDir = os.path.join(PODCASTDIR, 'prog')
sciDir = os.path.join(PODCASTDIR, 'sci')


quirks = Subscription(
    feed='http://www.cbc.ca/podcasting/includes/quirks.xml',
    targetDir=sciDir,
    renamer=Renamer('quirks').rename,
    count=10,
    name="Quirks & Quarks",
    days=[F, SA]
)


atissue = Subscription(
    feed='http://www.cbc.ca/podcasting/includes/atissue.xml',
    targetDir=NEWSDIR,
    renamer=Renamer('AtIssue').rename,
    count=3,
    name="At Issue",
    days=[W, TH, F]
)


otherpeoplesproblems = Subscription(
    feed='http://www.cbc.ca/podcasting/includes/opp.xml',
    targetDir=cbcDir,
    renamer=TitleRenamer('CBCOtherPeoplesProblems').rename,
    count=2,
    name="Other Peoples Problems",
    days=[M, W, F],  # Don't know when it comes out; distribute load
)


ondrugs = Subscription(
    feed='http://www.cbc.ca/podcasting/includes/ondrugs.xml',
    targetDir=cbcDir,
    renamer=TitleRenamer('CBCOnDrugs').rename,
    count=3,
    name="On Drugs",
    days=[SN, M, T,],
)


someoneknowssomething = Subscription(
    feed='http://www.cbc.ca/podcasting/includes/sks.xml',
    targetDir=cbcDir,
    renamer=TitleRenamer('CBCSomeoneKnowsSomething').rename,
    count=3,
    name="Someone Knows Something",
    days=[TH, F],
)


whitecoat = Subscription(
    feed='http://www.cbc.ca/podcasting/includes/whitecoat.xml',
    targetDir=sciDir,
    renamer=TitleRenamer('CBCWhiteCoatBlackArt').rename,
    count=5,
    name="White Coat Black Art",
    days=[SA, SN]
)


spark = Subscription(
    feed='http://www.cbc.ca/podcasting/includes/spark.xml',
    targetDir=cbcDir,
    renamer=TitleRenamer('CBCSpark').rename,
    count=3,
    name="Spark",
    days=WEEKEND
)


undertheinfluence = Subscription(
    feed='http://www.cbc.ca/podcasting/includes/undertheinfluence.xml',
    targetDir=cbcDir,
    renamer=TitleRenamer('CBCUnderTheInfluence').rename,
    count=2,
    name="Under The Influence",
    days=WEEKEND,
)


cbcSubscriptions = [
    quirks,
    atissue,
    otherpeoplesproblems,
    ondrugs,
    spark,
    whitecoat,
    undertheinfluence,
    someoneknowssomething,
]


gotime = Subscription(
    feed='https://changelog.com/gotime/feed',
    targetDir=programmingDir,
    count=8,
    name="GoTime",
    days=[SN, M, T],
)


hanselMinutes = Subscription(
    feed='https://rss.simplecast.com/podcasts/4669/rss',
    targetDir=programmingDir,
    count=8,
    renamer=TitleRenamer('hanselminutes').rename,
    name="HanselMinutes",
    days=[W, TH, F],
)


syntax = Subscription(
    feed='http://feed.syntax.fm/rss',
    targetDir=programmingDir,
    count=5,
    renamer=PostMp3StripTitleRenamer('Syntax').rename,
    name="Syntax",
    days=[F]
)


javascriptjabber = Subscription(
    feed='https://feeds.feedwrench.com/JavaScriptJabber.rss',
    targetDir=programmingDir,
    count=5,
    renamer=NullRenamer().rename,
    name="JavaScriptJabber",
    days=[M, TH, SA]
)


podcastinit = Subscription(
    feed='https://www.podcastinit.com/feed/mp3/',
    targetDir=programmingDir,
    count=10,
    renamer=TitleRenamer('Podcast.__init__').rename,
    name="Podcast.__init__",
    days=[W, SN]
)


testandcode = Subscription(
    feed='http://testandcode.com/rss/',
    targetDir=programmingDir,
    count=5,
    renamer=TitleRenamer('TestAndCode').rename,
    name="TestAndCode",
    days=[T, F]
)


talkpythontome = Subscription(
    feed='https://talkpython.fm/episodes/ogg_rss',
    targetDir=programmingDir,
    count=5,
    renamer=TitleITunesNumberRenamer("TalkPythonToMe").rename,
    name="TalkPythonToMe",
    days=[M, SA],
)


importthis = Subscription(
    feed='http://feeds.soundcloud.com/users/soundcloud:users:82237854/sounds.rss',
    targetDir=programmingDir,
    count=22,
    renamer=TitleRenamer("ImportThis").rename,
    name="ImportThis",
    days=[T]
)


fullstackradio = Subscription(
    feed='https://rss.simplecast.com/podcasts/279/rss',
    targetDir=programmingDir,
    count=10,
    renamer=TitleRenamer("FullStackRadio").rename,
    name="FullStackRadio",
    days=[W]
)


thechangelog = Subscription(
    feed='https://changelog.com/podcast/feed',
    targetDir=programmingDir,
    count=10,
    renamer=TitleRenamer("TheChangeLog").rename,
    name="TheChangeLog",
    days=[TH]
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
    targetDir=bbcDir,
    count=2,
    renamer=TitleRenamer("BBCAnalysis").rename,
    name="BBCAnalysis",
    days=[SN, M, T]
)


bbceverydayethics = Subscription(
    feed='http://www.bbc.co.uk/programmes/p02nrsmh/episodes/downloads.rss',
    targetDir=bbcDir,
    count=1,
    renamer=TitleRenamer("BBCEveryDayEthics").rename,
    name="BBCEveryDayEthics",
    days=WEEKEND,
)


bbclifescientific = Subscription(
    feed="http://www.bbc.co.uk/programmes/b015sqc7/episodes/downloads.rss",
    targetDir=sciDir,
    count=1,
    renamer=TitleRenamer("BBCLifeScientific").rename,
    name="BBCLifeScientific",
    days=[M, T, W]
)


bbcmediashow = Subscription(
    feed="http://www.bbc.co.uk/programmes/b00dv9hq/episodes/downloads.rss",
    targetDir=bbcDir,
    count=4,
    renamer=TitleRenamer("BBCMediaShow").rename,
    name="BBCMediaShow",
    days=[T, W, TH]
)


bbcspace = Subscription(
    feed="http://podcasts.files.bbci.co.uk/p03bv899.rss",
    targetDir=sciDir,
    count=3,
    renamer=TitleRenamer("BBCSpace").rename,
    name="BBCSpace",
    days=[SA, SN, M]
)


bbcprofile = Subscription(
    feed="http://www.bbc.co.uk/programmes/b006qjz5/episodes/downloads.rss",
    targetDir=bbcDir,
    count=1,
    renamer=TitleRenamer("BBCProfile").rename,
    name="BBCProfile",
    days=WEEKEND,
)


bbcipm = Subscription(
    feed='http://www.bbc.co.uk/programmes/p02nrtwc/episodes/downloads.rss',
    targetDir=bbcDir,
    count=1,
    renamer=TitleRenamer("BBCiPM").rename,
    name="BBCiPM",
    days=[TH, F, SA],
)


bbcdiscovery = Subscription(
    feed='https://podcasts.files.bbci.co.uk/p002w557.rss',
    targetDir=sciDir,
    count=1,
    renamer=TitleRenamer("BBCDiscovery").rename,
    name="BBCDiscovery",
    days=[SN, M, T]
)


bbcmoreorless = Subscription(
    feed='http://www.bbc.co.uk/programmes/p02nrss1/episodes/downloads.rss',
    targetDir=bbcDir,
    count=1,
    renamer=TitleRenamer("BBCMoreOrLess").rename,
    name="BBCMoreOrLess",
    days=ALLWEEK,
)


bbcwhyfactor = Subscription(
    feed='http://www.bbc.co.uk/programmes/p00xtky9/episodes/downloads.rss',
    targetDir=bbcDir,
    count=1,
    renamer=TitleRenamer("BBCWhyFactor").rename,
    name="BBCWhyFactor",
    days=[SN, M, T]
)


bbcwitness = Subscription(
    feed='http://www.bbc.co.uk/programmes/p004t1hd/episodes/downloads.rss',
    targetDir=bbcDir,
    count=7,
    renamer=TitleRenamer("BBCWitness").rename,
    name="BBCWitness",
    days=WEEKDAYS,
)


bbcdrkarl = Subscription(
    feed='https://podcasts.files.bbci.co.uk/p02pc9ny.rss',
    targetDir=sciDir,
    count=3,
    # Leaving it as title to see if it distinguishes dr karl from non
    renamer=TitleRenamer("BBCDrKarl").rename,
    name="BBCDrKarl",
    days=[W, TH, F, SA, SN, M]
)


bbcclick = Subscription(
    feed='http://www.bbc.co.uk/programmes/p002w6r2/episodes/downloads.rss',
    targetDir=geekDir,
    count=1,
    renamer=TitleRenamer("BBCClick").rename,
    name="BBCClick",
    days=[M, T, W]
)


bbceddiemair = Subscription(
    feed='http://www.bbc.co.uk/programmes/p03m4q5s/episodes/downloads.rss',
    targetDir=bbcDir,
    count=1,
    renamer=TitleRenamer("BBCEddieMair").rename,
    name="BBCEddieMair",
    days=WEEKEND
)


bbctechtent = Subscription(
    feed='http://www.bbc.co.uk/programmes/p01plr2p/episodes/downloads.rss',
    targetDir=geekDir,
    count=1,
    renamer=TitleRenamer("BBCTechTent").rename,
    name="BBCTechTent",
    days=[TH, F, SA]
)


bbcfileonfour = Subscription(
    feed='https://podcasts.files.bbci.co.uk/b006th08.rss',
    targetDir=bbcDir,
    count=4,
    renamer=TitleRenamer("BBCFileOnFour").rename,
    name="BBCFileOnFour",
    days=[M, T, W]
)


bbcscienceinaction = Subscription(
    feed='http://www.bbc.co.uk/programmes/p002vsnb/episodes/downloads.rss',
    targetDir=sciDir,
    count=1,
    renamer=Renamer("BBCScienceInAction").rename,
    name="BBCScienceInAction",
    days=[W, TH, F]
)


bbcgreatlives = Subscription(
    feed='http://www.bbc.co.uk/programmes/b006qxsb/episodes/downloads.rss',
    targetDir=bbcDir,
    count=2,
    renamer=TitleRenamer("BBCGreatLives").rename,
    name="BBCGreatLives",
    days=[M, T, W]
)


bbcinourtime = Subscription(
    feed='http://www.bbc.co.uk/programmes/b006qykl/episodes/downloads.rss',
    targetDir=bbcDir,
    count=1,
    renamer=TitleRenamer("BBCInOurTime").rename,
    name="BBCInOurTime",
    days=[W, TH, F]
)


bbcmoralmaze = Subscription(
    feed='http://www.bbc.co.uk/programmes/b006qk11/episodes/downloads.rss',
    targetDir=bbcDir,
    count=1,
    renamer=TitleRenamer("BBCMoralMaze").rename,
    name="BBCMoralMaze",
    days=[T, W, TH],
)


bbcr4report = Subscription(
    feed='http://www.bbc.co.uk/programmes/b00jkr1q/episodes/downloads.rss',
    targetDir=bbcDir,
    count=1,
    renamer=TitleRenamer("BBCR4Report").rename,
    name="BBCR4Report",
    days=[W, TH, F],
)


bbcinsidescience = Subscription(
    feed='http://www.bbc.co.uk/programmes/b036f7w2/episodes/downloads.rss',
    targetDir=sciDir,
    count=1,
    renamer=TitleRenamer("BBCInsideScience").rename,
    name="BBCInsideScience",
    days=[W, TH, F]
)


bbcmonkeycage = Subscription(
    feed='http://www.bbc.co.uk/programmes/b00snr0w/episodes/downloads.rss',
    targetDir=sciDir,
    count=1,
    renamer=TitleRenamer("BBCMonkeyCage").rename,
    name="BBCMonkeyCage",
    days=[SN, M, T]
)


bbcreithlectures = Subscription(
    feed='http://podcasts.files.bbci.co.uk/b00729d9.rss',
    targetDir=bbcDir,
    count=1,
    renamer=TitleRenamer("BBCReithLectures").rename,
    name="BBCReithLectures",
)

bbcdeathinicevalley = Subscription(
    feed='http://podcasts.files.bbci.co.uk/p060ms2h.rss',
    targetDir=bbcDir,
    count=5,
    renamer=TitleRenamer("BBCDeathInIceValley").rename,
    name="BBCDeathInIceValley",
    days=[SN, M, T]
)



bbcSubscriptions = [
    bbceverydayethics,
    bbcipm,
    bbcwhyfactor,
    bbcmoreorless,
    bbcmoralmaze,
    bbcprofile,
    bbcmediashow,
    bbcfileonfour,
    bbcinourtime,
    bbcr4report,
    bbcanalysis,
    bbcwitness,
    bbcgreatlives,
    bbceddiemair,
    bbcreithlectures,
    bbcdeathinicevalley,
]


philosophybites = Subscription(
    feed='http://www.philosophybites.libsyn.com/rss',
    targetDir=philDir,
    count=5,
    renamer=PostMp3StripTitleRenamer("PhilosophyBites").rename,
    name="PhilosophyBites"
)


philosophySubscriptions = [
    philosophybites,
]


thePenAddict = Subscription(
    feed='https://www.relay.fm/penaddict/feed',
    targetDir=penDir,
    count=2,
    renamer=NullRenamer().rename,
    name="The Pen Addict",
    days=[T, W, TH],
)


goulet = Subscription(
    feed='http://feeds.feedburner.com/GouletQa',
    targetDir=penDir,
    count=5,
    renamer=NullRenamer().rename,
    name="Goulet",
    days=[F],
)




class TenPerRenamer(Renamer):
    """Dedicated renamer for the 10% Happier Podcast"""
    def _generateName(self, url, stamp, entry, idn):
        number = entry.title.split(':')[0].strip('#')
        num = self._getIDNumerPart(idn)
        return f"10PercentHappier_{number}{num}.mp3"


tenpercenthappier = Subscription(
    feed='http://feeds.feedburner.com/abcradio/10percenthappier?format=xml',
    targetDir='/home/brian/media/podcasts/podpad2/buddhist',
    count=2,
    renamer=TenPerRenamer().rename,
    name="Ten Percent Happier",
    days=[T, W, TH]
)


ninety9percentinvisible = Subscription(
    feed='http://feeds.99percentinvisible.org/99percentinvisible',
    targetDir=geekDir,
    count=5,
    renamer=TitleRenamer('99PercentInvisible').rename,
    name="99 Percent Invisible"
)


allinthemind = Subscription(
    feed='http://www.abc.net.au/radionational/feed/2888650/podcast.xml',
    targetDir=sciDir,
    count=2,
    renamer=TitleRenamer("AllInTheMind").rename,
    name="AllInTheMind",
    days=[T, TH, SA]
)


ockhamsrazor = Subscription(
    feed='http://www.abc.net.au/radionational/feed/2883682/podcast.xml',
    targetDir=sciDir,
    count=5,
    renamer=TitleRenamer("OckhamsRazor").rename,
    name="OckhamsRazor",
    days=[SA,]
)


sixtysecondscience = Subscription(
    feed='http://rss.sciam.com/sciam/60secsciencepodcast?format=xml',
    targetDir=sciDir,
    count=5,
    renamer=PostMp3StripTitleRenamer("SixtySecondScience").rename,
    name="SixtySecondScience",
    days=[M, W, F, SA]
)


greatmomentsinscience = Subscription(
    feed='http://www.abc.net.au/radionational/feed/7417248/podcast.xml',
    targetDir=sciDir,
    count=10,
    renamer=TitleRenamer("GreatMomentsInScience").rename,
    name="GreatMomentsInScience",
    days=[T],
)


thescienceshow = Subscription(
    feed='http://www.abc.net.au/radionational/feed/2885486/podcast.xml',
    targetDir=sciDir,
    count=30,
    renamer=TitleRenamer("TheScienceShow").rename,
    name="TheScienceShow",
    days=WEEKEND,
)


spacetime = Subscription(
    feed='https://audioboom.com/channels/4642443.rss',
    targetDir=sciDir,
    count=3,
    renamer=TitleRenamer("SpaceTime").rename,
    name="SpaceTime",
    days=[T, ],
)


enginesofingenuity = Subscription(
    feed='https://www.houstonpublicmedia.org/podcasts/engines-of-our-ingenuity/',
    targetDir=sciDir,
    count=30,
    renamer=TitleRenamer("Engines").rename,
    name="Engines Of Our Ingenuity",
    days=[T, TH, SN]
)


sciencepodcasts = [
    sixtysecondscience,
    greatmomentsinscience,
    bbclifescientific,
    bbcinsidescience,
    bbcdrkarl,
    bbcmonkeycage,
    bbcdiscovery,
    bbcscienceinaction,
    thescienceshow,
    allinthemind,
    ockhamsrazor,
    bbcspace,
    enginesofingenuity,
]


heresthething = Subscription(
    feed='http://feeds.wnyc.org/wnycheresthething',
    targetDir=geekDir,
    count=3,
    renamer=TitleRenamer('HeresTheThing').rename,
    name="HeresTheThing",
    days=[M, W, F]
)


downloadthisshow = Subscription(
    feed='http://www.abc.net.au/radionational/feed/3777916/podcast.xml',
    targetDir=geekDir,
    count=2,
    renamer=TitleRenamer('DownloadThisShow').rename,
    name="DownloadThisShow",
    days=[T, TH, SA],
)


futuretense = Subscription(
    feed='http://www.abc.net.au/radionational/feed/2883726/podcast.xml',
    targetDir=geekDir,
    count=5,
    renamer=TitleRenamer('FutureTense').rename,
    name="FutureTense",
    days=[SN]
)


thephilosopherszone = Subscription(
    feed='http://www.abc.net.au/radionational/feed/2884506/podcast.xml',
    targetDir=philDir,
    count=5,
    renamer=TitleRenamer('ThePhilosophersZone').rename,
    name="ThePhilosophersZone",
    days=[TH]
)


beyondthetodolist = Subscription(
    feed="http://feeds2.noodle.mx/beyondthetodolist",
    targetDir=geekDir,
    count=1,
    renamer=TitleRenamer('BeyondTheToDoList').rename,
    name="BeyondTheToDoList",
    days=[SA],
)


trumpconlaw = Subscription(
    feed="http://feeds.trumpconlaw.com/TrumpConLaw",
    targetDir=geekDir,
    count=5,
    renamer=TitleRenamer('WhatTrumpCanTeachAboutConLaw').rename,
    name="WhatTrumpCanTeachAboutConLaw",
    days=[T, F, SN],
)


geekSubscriptions = [
    trumpconlaw,
    ninety9percentinvisible,
    thePenAddict,
    bbcclick,
    bbctechtent,
    heresthething,
    downloadthisshow,
    goulet,
    tenpercenthappier,
    futuretense,
    beyondthetodolist,
    thephilosopherszone,
]


ubunutuuk = Subscription(
    feed="http://ubuntupodcast.org/feed/podcast",
    targetDir=linuxDir,
    count=1,
    renamer=TitleRenamer('UbuntuUK').rename,
    name="UbuntuUK",
    days=[T, W, TH, SA]
)


linuxvoice = Subscription(
    feed="http://www.linuxvoice.com/podcast_ogg.rss",
    targetDir=linuxDir,
    count=1,
    renamer=TitleRenamer('LinuxVoice').rename,
    name="LinuxVoice"
)


flossweekly = Subscription(
    feed="http://feeds.twit.tv/floss.xml",
    targetDir=linuxDir,
    count=5,
    renamer=NullRenamer().rename,
    name="FLOSSWeekly",
    days=[M],
)


linuxSubscriptions = [
    linuxvoice,
    flossweekly,
    ubunutuuk,
]




newsSubscriptions = [
]
newsSubscriptions.extend(NewsSubscriptions)


subscriptions = []
for sub in [
        newsSubscriptions,
        bbcSubscriptions,
        cbcSubscriptions,
        sciencepodcasts,
        programmingSubscriptions,
        geekSubscriptions,
        linuxSubscriptions,]:
    subscriptions.extend(sub)


#############################################################################
###
###    Retires, defunct, or otherwise inactive:
###
bbcfiftythings = Subscription(
    feed='http://podcasts.files.bbci.co.uk/p04b1g3c.rss',
    targetDir=bbcDir,
    count=55,
    renamer=TitleRenamer("BBCFiftyThingsThatMadeTheModernEconomy").rename,
    name="BBCFiftyThingsThatMadeTheModernEconomy",
)
