import plistlib
import os

file_path = 'void/waitwhat/Semantic satiation - Wikipedia.webarchive'

try:
    with open(file_path, 'rb') as f:
        pl = plistlib.load(f)
        
    if 'WebMainResource' in pl and 'WebResourceData' in pl['WebMainResource']:
        html_data = pl['WebMainResource']['WebResourceData']
        # WebResourceData is bytes
        html_content = html_data.decode('utf-8', errors='replace')
        
        # Save to a temp file so I can read it properly with read_file or just print a snippet
        with open('extracted_wiki.html', 'w', encoding='utf-8') as out:
            out.write(html_content)
            
        print("Successfully extracted HTML to extracted_wiki.html")
    else:
        print("Could not find WebMainResource/WebResourceData in plist")

except Exception as e:
    print(f"Error: {e}")

