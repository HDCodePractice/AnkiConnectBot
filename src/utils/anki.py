import genanki


hd_model = genanki.Model(
    model_id=1260907439,
    name="老房东词汇模板",
    fields=[
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
    ],
    templates=[
        {
            "name": "Card1",
            'qfmt': """<div class="front">
  <h1>{{Vocabulary}}</h1>
  <p>{{Pronunciations}}</p>
  <hr>
  {{SoundVocabulary}}{{SoundExample}}  
</div>
""",
            'afmt': """{{FrontSide}}
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
        },
    ],
    css=""".card {
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
)

# Add your notes here, replacing sensitive data with placeholders
hd_note = genanki.Note(
    model=hd_model,
    fields=[
        "light",
        "/laɪt/",
        "lighter, lightest",
        "adj. having little weight",
        "轻的",
        "This suitcase is very light.",
        "这个箱子非常轻。",
        "[sound:light.mp3]",
        "[sound:light_meaning.mp3]",
        "[sound:light_example.mp3]",
        '<img src="light.jpg">'
    ],
)

# Use my_card object for further processing or export
hd_deck = genanki.Deck(
    1260907438,
    '老房东的单词本'
)

hd_deck.add_note(hd_note)
hd_package = genanki.Package(hd_deck)
hd_package.media_files = ['res/light.jpg', 'res/light.mp3',
                          'res/light_example.mp3', 'res/light_meaning.mp3']
hd_package.write_to_file('hdbook.apkg')
