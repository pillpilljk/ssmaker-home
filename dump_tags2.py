with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('const tagTranslations = {')
with open('tag_trans2.txt', 'w', encoding='utf-8') as out:
    if idx != -1:
        out.write(text[idx+1800:idx+3500])

print("Done")
