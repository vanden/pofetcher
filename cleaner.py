import datetime
import os

from config import NEWSDIR

now = datetime.datetime.now()

# I don't want to immediately fall into the trap of making classes. I don't
# expect this to extend very far, so YAGNI and the simplest thing that could
# possibly work

HOURLYNEWSLAG = datetime.timedelta(seconds=60*60*1.2)

with os.scandir(NEWSDIR) as targetDir:
    for entry in targetDir:
        
        if 'Week' in entry.path:
            continue

        modtime = datetime.datetime.fromtimestamp(entry.stat().st_mtime)

        if 'WorldAtSix' in entry.path or 'BBCNewsHour' in entry.path:
            # These ones come less often, so don't kill them unless rather old.
            if now - modtime > HOURLYNEWSLAG * 8:
                os.remove(entry.path)
        else:
            if now - modtime > HOURLYNEWSLAG:
                os.remove(entry.path)
