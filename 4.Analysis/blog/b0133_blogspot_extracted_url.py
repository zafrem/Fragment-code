import re

def extract_urls(text):
    url_pattern = r'https?://[^\s]+?<'
    urls = re.findall(url_pattern, text)
    return urls

with open("sitemap.xml", "r") as f:
    line = f.readline()
    extracted_urls = extract_urls(line)

for item in extracted_urls:
    if 'http://www.sitemaps.org' in item:
        continue
    print(item[:-1])
