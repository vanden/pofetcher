import feedparser

#feed_to_explore = "https://rss.simplecast.com/podcasts/4669/rss"
feed_to_explore = "http://www.cbc.ca/podcasting/includes/quirks.xml"
feed = feedparser.parse(feed_to_explore)
if 'title' in feed:
    print(f"Feed title: {feed.title}")
    print()

for entry in feed['entries']:
    # print(entry)
    # print(dir(entry))
    # print(entry.keys)
    # print(entry.keys())
    # print(entry.enclosures[0])
    # print(entry.enclosures[0].href)
#    input()

    if 'author' in entry:
        print(f"author of entry: {entry.author}\n\n\n")
    if 'author_detail' in entry:
        print(f"author_detail of entry: {entry.author_detail}\n\n\n")
    if 'authors' in entry:
        print(f"authors of entry: {entry.authors}\n\n\n")
    if 'contents' in entry:
        print(f"Contents of entry: {entry.contents}\n\n\n")
    if 'content' in entry:
        print(f"content of entry: {entry.content}\n\n\n")
    if 'comments' in entry:
        print(f"Comments of entry: {entry.comments}\n\n\n")
    if 'created_parsed' in entry:
        print(f"Created_parsed: {entry.created_parsed}\n\n\n")
    if 'enclosures' in entry:
        print(f"Enclosures length: {len(entry.enclosures)}\n\n\n")
        if len(entry.enclosures):
            print(f"Enclosure the first: {entry.enclosures[0]}\n\n\n")
    if 'enclosure' in entry:
        print(f"Enclosure: {entry.enclosure}\n\n\n")
    if 'guidislink' in entry:
        print(f"guidislink of entry: {entry.guidislink}\n\n\n")
    if 'id' in entry:
        print(f"id of entry: {entry.id}\n\n\n")
    if 'image' in entry:
        print(f"image of entry: {entry.image}\n\n\n")
    if 'itunes_duration' in entry:
        print(f"itunes_duration of entry: {entry.itunes_duration}\n\n\n")
    if 'itunes_episode' in entry:
        print(f"itunes_episode of entry: {entry.itunes_episode}\n\n\n")
    if 'itunes_episodetype' in entry:
        print(f"itunes_episodetype of entry: {entry.itunes_episodetype}\n\n\n")
    if 'itunes_explicit' in entry:
        print(f"itunes_explicit of entry: {entry.itunes_explicit}\n\n\n")
    if 'links' in entry:
        print(f"links of entry: {entry.links}\n\n\n")
    if 'published' in entry:
        print(f"published of entry: {entry.published}\n\n\n")
    if 'published_parsed' in entry:
        print(f"published_parsed of entry: {entry.published_parsed}\n\n\n")
    if 'source' in entry:
        print(f"Source of entry: {entry.source}\n\n\n")
    if 'subtitle' in entry:
        print(f"subtitle of entry: {entry.subtitle}\n\n\n")
    if 'subtitle_detail' in entry:
        print(f"subtitle_detail of entry: {entry.subtitle_detail}\n\n\n")
    if 'summary' in entry:
        print(f"summary of entry: {entry.summary}\n\n\n")
    if 'summary_detail' in entry:
        print(f"summary_detail of entry: {entry.summary_detail}\n\n\n")
    if 'tags' in entry:
        print(f"Tags of entry: {entry.tags}\n\n\n")
    if 'title' in entry:
        print(f"title of entry: {entry.title}\n\n\n")
    if 'title_detail' in entry:
        print(f"title_detail of entry: {entry.title_detail}\n\n\n")

    print(entry.keys())

    raise
    print()
