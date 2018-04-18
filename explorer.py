import feedparser, requests

#feed_to_explore = "https://rss.simplecast.com/podcasts/4669/rss"
feed_to_explore = "http://www.cbc.ca/podcasting/includes/quirks.xml"
feed = feedparser.parse(feed_to_explore)
if 'title' in feed:
    print(f"Feed title: {feed.title}")
    print()
for entry in feed['entries']:

    if 'author' in entry:
        print(f"author of entry: {entry.author}")
    if 'author_detail' in entry:
        print(f"author_detail of entry: {entry.author_detail}")
    if 'authors' in entry:
        print(f"authors of entry: {entry.authors}")
    if 'contents' in entry:
        print(f"Contents of entry: {entry.contents}")
    if 'content' in entry:
        print(f"content of entry: {entry.content}")
    if 'comments' in entry:
        print(f"Comments of entry: {entry.comments}")
    if 'created_parsed' in entry:
        print(f"Created_parsed: {entry.created_parsed}")
    if 'enclosures' in entry:
        print(f"Enclosures length: {len(entry.enclosures)}")
        print(f"Enclosure the first: {entry.enclosures[0]}")
    if 'guidislink' in entry:
        print(f"guidislink of entry: {entry.guidislink}")
    if 'id' in entry:
        print(f"id of entry: {entry.id}")
    if 'image' in entry:
        print(f"image of entry: {entry.image}")
    if 'itunes_duration' in entry:
        print(f"itunes_duration of entry: {entry.itunes_duration}")
    if 'itunes_episode' in entry:
        print(f"itunes_episode of entry: {entry.itunes_episode}")
    if 'itunes_episodetype' in entry:
        print(f"itunes_episodetype of entry: {entry.itunes_episodetype}")
    if 'itunes_explicit' in entry:
        print(f"itunes_explicit of entry: {entry.itunes_explicit}")
    if 'links' in entry:
        print(f"links of entry: {entry.links}")
    if 'published' in entry:
        print(f"published of entry: {entry.published}")
    if 'published_parsed' in entry:
        print(f"published_parsed of entry: {entry.published_parsed}")
    if 'source' in entry:
        print(f"Source of entry: {entry.source}")
    if 'subtitle' in entry:
        print(f"subtitle of entry: {entry.subtitle}")
    if 'subtitle_detail' in entry:
        print(f"subtitle_detail of entry: {entry.subtitle_detail}")
    if 'summary' in entry:
        print(f"summary of entry: {entry.summary}")
    if 'summary_detail' in entry:
        print(f"summary_detail of entry: {entry.summary_detail}")
    if 'tags' in entry:
        print(f"Tags of entry: {entry.tags}")
    if 'title' in entry:
        print(f"title of entry: {entry.title}")
    if 'title_detail' in entry:
        print(f"title_detail of entry: {entry.title_detail}")
    for k in entry:
        print(k)
        print()

    print(entry.keys())

    raise
    print()
