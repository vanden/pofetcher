import feedparser, requests

feed_to_explore = "https://changelog.com/gotime/feed"

feed = feedparser.parse(feed_to_explore)
if 'title' in feed:
    print(f"Feed title: {feed.title}")
    print()
for entry in feed['entries']:
    if 'enclosures' in entry:
        print(f"Enclosures length: {len(entry.enclosures)}")
        print(f"Enclosure the first: {entry.enclosures[0]}")

    if 'published_parsed' in entry:
        print(f"Published_parsed: {entry.published_parsed}")
        
    if 'created_parsed' in entry:
        print(f"Created_parsed: {entry.created_parsed}")
    print()
    
