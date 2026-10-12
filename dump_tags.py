with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
idx = text.find('const tagTranslations = {')
with open('tag_trans.txt', 'w', encoding='utf-8') as out:
    if idx != -1:
        out.write(text[idx:idx+2500])

print("Done")
