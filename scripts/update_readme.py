import feedparser

RSS_URL = "https://blog.roshanacharya.info.np/rss.xml"
MAX_POSTS = 5

# Parse RSS
feed = feedparser.parse(RSS_URL)
posts = feed.entries[:MAX_POSTS]

# Build Markdown list
md = "\n".join([f"- [{p.title}]({p.link})" for p in posts])

# Read README
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

start = "<!-- HASHNODE-POSTS:START -->"
end = "<!-- HASHNODE-POSTS:END -->"

before = content.split(start)[0]
after = content.split(end)[-1]

new_content = f"{before}{start}\n{md}\n{end}{after}"

# Write back
with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)
