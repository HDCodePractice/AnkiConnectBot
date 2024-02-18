import genanki
from carddb import CardDBHelper
import os

fields = [
    {"name": "Vocabulary", "type": "string"},
    {"name": "Pronunciations", "type": "string"},
    {"name": "Forms", "type": "string"},
    {"name": "Meaning", "type": "text"},
    {"name": "ChineseMeaning", "type": "text"},
    {"name": "Example", "type": "text"},
    {"name": "ChineseExample", "type": "text"},
    {"name": "SoundVocabulary", "type": "audio"},
    {"name": "SoundMeaning", "type": "audio"},
    {"name": "SoundExample", "type": "audio"},
    {"name": "Image", "type": "image"}
]

front = """<div class="front">
    <h1>{{Vocabulary}}</h1>
    <p>{{Pronunciations}}</p>
    <hr>
    {{SoundVocabulary}}{{SoundExample}}  
</div>
"""

backend = """{{FrontSide}}
<div class="back">
    <p class="example">{{Example}}</p>
    <p class="example">{{hint:ChineseExample}}</p>
    {{Image}}
    <hr>
    <p class="meaning">{{Meaning}}</p>
    <p class="meaning">{{hint:ChineseMeaning}}</p>
    <hr>
    <div>
        {{SoundMeaning}}
    </div>
</div>
"""

css = """.card {
    font-family: Arial, sans-serif;
    background-color: Black;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 15px;
}

/* Front of the card */
.front {
    text-align: center;
}

.front h1 {
    font-size: 24px;
    color: #FF80DD;
}

.front p {
    font-size: 18px;
    color: #666;
}

/* Back of the card */
.back {
    text-align: center;
}

.back img {
    max-width: 150px;
    max-height: 150px;
    margin-bottom: 10px;
}

.meaning {
    font-size: 16px;
    color:#00aaaa; 
    text-align:left;
}

.meaning a {
	text-decoration: none;
	padding: 1px 6px 2px 5px;
	margin: 0 5px 0 0;
	font-size: 12px;
	color: white;
	font-weight: normal;
	border-radius: 4px
}

.meaning a.pos_n {
    background-color: #e3412f
}

.meaning a.pos_v {
    background-color: #539007
}

.meaning a.pos_adj {
    background-color: #f7b125
}

.meaning a.pos_adv {
    background-color: #0271f7
}

.meaning a.pos_prep {
    background-color: #684b9d
}

.meaning a.pos_conj {
    background-color: #ff00ff
}

.meaning a.pos_pron {
    background-color: #00ffff
}

.meaning a.pos_interj {
    background-color: #d8d832
}

.example {
    font-size: 16px;
    color:#9CFFFA; 
    text-align:left;
}

.hint {
    font-size: 16px;
    color: #CCCCCC; 
    text-align:left;
    border: 1px dashed #ccc;
    padding: 2px;
    border-radius: 5px;
}

/* Audio controls */
audio {
    margin-bottom: 10px;
}

img{
        max-width:100%;
        height:auto;
        width:300px;
        border-radius: 20px;
}
"""

pos_format = {
    "noun": "<a class='pos_n'>n. </a>",
    "verb": "<a class='pos_v'>v. </a>",
    "adjective": "<a class='pos_adj'>adj. </a>",
    "adverb": "<a class='pos_adv'>adv. </a>",
    "preposition": "<a class='pos_prep'>prep. </a>",
    "conjunction": "<a class='pos_conj'>conj. </a>",
    "pronoun": "<a class='pos_pron'>pron. </a>",
    "interjection": "<a class='pos_interj'>interj. </a>"
}


def create_hd_deck():
    card_db = CardDBHelper("cards.db")
    cards = card_db.get_all_cards()
    hd_model = genanki.Model(
        model_id=1260907439,
        name="老房东词汇模板",
        fields=fields,
        templates=[{
            "name": "Card1",
            'qfmt': front,
            'afmt': backend
        }],
        css=css)

    hd_deck = genanki.Deck(
        1260907438,
        '老房东的单词本'
    )

    media_files = []
    # check res folder, if doesn't exist, create it
    if not os.path.exists('res'):
        os.makedirs('res')
    for card in cards:
        card_id, vocabulary, pronunciation, part_of_speech, \
            forms, meaning, chinese_meaning, example, chinese_example, \
            sound_vocabulary, sound_meaning, sound_example, image = card

        if sound_vocabulary:
            with open(f'res/{card_id}.mp3', 'wb') as f:
                f.write(sound_vocabulary)
            media_files.append(f'res/{card_id}.mp3')

        if sound_meaning:
            with open(f'res/{card_id}_m.mp3', 'wb') as f:
                f.write(sound_meaning)
            media_files.append(f'res/{card_id}_m.mp3')

        if sound_example:
            with open(f'res/{card_id}_e.mp3', 'wb') as f:
                f.write(sound_example)
            media_files.append(f'res/{card_id}_e.mp3')

        if image:
            with open(f'res/{card_id}.jpg', 'wb') as f:
                f.write(image)
            media_files.append(f'res/{card_id}.jpg')

        pos = pos_format.get(part_of_speech, f"{part_of_speech}.")

        hd_note = genanki.Note(
            model=hd_model,
            fields=[
                vocabulary,
                pronunciation,
                forms,
                f"{pos}{meaning}",
                f"{pos}{chinese_meaning}",
                example,
                chinese_example,
                f"[sound:{card_id}.mp3]" if sound_vocabulary else "",
                f"[sound:{card_id}_m.mp3]" if sound_meaning else "",
                f"[sound:{card_id}_e.mp3]" if sound_example else "",
                f'<img src="{card_id}.jpg">' if image else ''
            ])
        hd_deck.add_note(hd_note)

    hd_package = genanki.Package(hd_deck)
    hd_package.media_files = media_files
    hd_package.write_to_file('hdbook.apkg')


if __name__ == "__main__":
    create_hd_deck()
