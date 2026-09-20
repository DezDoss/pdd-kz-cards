#!/bin/sh
# Две сборки из одного шаблона:
#   index.html      — для публикации артефактом (обёртку <head> ставит хост)
#   dist/index.html — самостоятельная PWA: свой <head>, манифест, service worker
cd "$(dirname "$0")"
python3 - <<'PY'
import json
cards = json.load(open('cards.json'))
raw = json.dumps(cards, ensure_ascii=False, separators=(',',':')).replace('</', '<\\/')
body = open('app.template.html', encoding='utf-8').read().replace('__CARDS_JSON__', raw)

open('index.html', 'w', encoding='utf-8').write(body)

head = open('head.html', encoding='utf-8').read()
tail = open('tail.html', encoding='utf-8').read()
open('dist/index.html', 'w', encoding='utf-8').write(head + body + tail)
print('index.html      ', len(body.encode()), 'байт')
print('dist/index.html ', len((head+body+tail).encode()), 'байт,', len(cards), 'карточек')
PY
