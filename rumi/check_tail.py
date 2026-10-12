with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'꼬리잡기', text)]
with open('tail_matches.txt', 'w', encoding='utf-8') as out:
    out.write(f"Matches for 꼬리잡기: {len(matches)}\n")
    for m in matches:
        out.write(text[m-60:m+80].replace('\n', ' ') + "\n")

print("Done")
