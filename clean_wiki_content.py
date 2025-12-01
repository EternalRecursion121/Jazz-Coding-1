from bs4 import BeautifulSoup

with open('extracted_wiki.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Extract heading
heading = soup.find(id='firstHeading')

# Extract body content
body = soup.find(id='bodyContent')

# Clean up body
# Remove all script, style, link tags from body
for tag in body.find_all(['script', 'style', 'link', 'meta']):
    tag.decompose()

# Remove some nav elements inside bodyContent if any (like siteSub, contentSub if we don't want them, but they add realism)
# I'll keep them for realism.

# Create a new container
container = soup.new_tag('div')
if heading:
    container.append(heading)
if body:
    container.append(body)

# Convert to string
html_out = str(container)

with open('clean_wiki_snippet.html', 'w', encoding='utf-8') as f:
    f.write(html_out)

print("Cleaned HTML saved to clean_wiki_snippet.html")

