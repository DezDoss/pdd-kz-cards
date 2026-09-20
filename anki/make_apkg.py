# -*- coding: utf-8 -*-
"""Колода Anki из cards.json — с теми же картинками (инлайновый SVG рендерится в Anki)."""
import json, os, genanki

HERE = os.path.dirname(os.path.abspath(__file__))
cards = json.load(open(os.path.join(HERE, "..", "cards.json"), encoding="utf-8"))

CSS = """
.card { font-family: -apple-system, "Helvetica Neue", Arial, sans-serif; font-size: 19px;
        text-align: left; color: #141a22; background: #f6f7f9; padding: 16px 18px; line-height: 1.5; }
.lbl { font-family: ui-monospace, Menlo, monospace; font-size: 10.5px; letter-spacing: .16em;
       text-transform: uppercase; color: #77818f; display: block; margin-bottom: 8px; }
.q { font-size: 21px; font-weight: 600; line-height: 1.4; }
.a { font-size: 19px; line-height: 1.5; }
.a b { color: #1b5cb8; }
hr#answer { border: 0; border-top: 1px solid #cfd6df; margin: 15px 0; }
svg { display: block; margin: 10px auto; max-width: 100%; height: auto; }
.nightMode.card { color: #e6ebf2; background: #10141a; }
.nightMode .lbl { color: #7a8493; }
.nightMode .a b { color: #79adf5; }
.nightMode hr#answer { border-top-color: #2c3540; }
"""

model = genanki.Model(
    1728394501, "ПДД РК — вопрос/ответ",
    fields=[{"name": "Вопрос"}, {"name": "Ответ"}, {"name": "Тема"}],
    templates=[{"name": "Карточка",
                "qfmt": "{{Вопрос}}",
                "afmt": '{{Вопрос}}<hr id="answer">{{Ответ}}'}],
    css=CSS)

decks, order = {}, []
for c in cards:
    if c["deck"] not in decks:
        order.append(c["deck"])
        decks[c["deck"]] = genanki.Deck(1728394600 + len(order), "ПДД Казахстан 2026::" + c["deck"])
    decks[c["deck"]].add_note(genanki.Note(
        model=model, fields=[c["front"], c["back"], c["deck"]],
        tags=["ПДД_РК"] + [t.replace(" ", "_") for t in c["tags"]]))

path = os.path.join(HERE, "PDD-KZ-2026.apkg")
genanki.Package([decks[d] for d in order]).write_to_file(path)
print("apkg:", os.path.getsize(path), "байт ·", len(cards), "карточек ·", len(order), "подколод")

with open(os.path.join(HERE, "PDD-KZ-2026.tsv"), "w", encoding="utf-8") as f:
    f.write("#separator:tab\n#html:true\n#deck column:1\n#tags column:4\n")
    for c in cards:
        f.write("\t".join(["ПДД Казахстан 2026::" + c["deck"], c["front"], c["back"],
                           " ".join(t.replace(" ", "_") for t in c["tags"])]) + "\n")
print("tsv готов")
