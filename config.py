"""Provides some common configuration elements"""

import os

PODCASTDIR = '/home/brian/media/podcasts/podpad2'
PODLOG = os.path.join(PODCASTDIR, 'podfetchlog')
NEWSDIR = os.path.join(PODCASTDIR, 'news')

M, T, W, TH, F, S, SN = range(7)
SA = S
WEEKDAYS = [M, T, W, TH, F]
WEEKEND = [F, S, SN, M]
ALLWEEK = [M, T, W, TH, F, S, SN]
