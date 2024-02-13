import sqlite3
from sqlite3 import Error
import os


class CardDBHelper:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None
        try:
            if not os.path.exists(self.db_file):
                self.create_database()
            self.connection = sqlite3.connect(self.db_file)
        except Error as e:
            print(e)

    def create_database(self):
        try:
            connection = sqlite3.connect(self.db_file)
            cursor = connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS cards (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Vocabulary TEXT,
                    Pronunciation TEXT,
                    PartOfSpeech TEXT,
                    Forms TEXT,
                    Meaning TEXT,
                    Example TEXT,
                    ChineseExample TEXT,
                    SoundVocabulary BLOB NULL,
                    SoundMeaning BLOB NULL,
                    SoundExample BLOB NULL,
                    Image BLOB NULL
                )
            ''')
            connection.commit()
            connection.close()
        except Error as e:
            print(e)

    def insert_card(self, card_data):
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO cards (Vocabulary, Pronunciation, PartOfSpeech, Forms, Meaning, Example, ChineseExample)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', card_data)
            self.connection.commit()
            return cursor.lastrowid
        except Error as e:
            print(e)
            return 0

    def get_card_id_by_vocabulary_and_example(self, vocabulary, example):
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                SELECT ID FROM cards WHERE Vocabulary = ? AND Example = ?
            ''', (vocabulary, example))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return None
        except Error as e:
            print(e)

    def update_sound_files_by_id(self, card_id, sound_vocabulary_path, sound_meaning_path, sound_example_path):
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                UPDATE cards SET SoundVocabulary = ?, SoundMeaning = ?, SoundExample = ? WHERE ID = ?
            ''', (sound_vocabulary_path, sound_meaning_path, sound_example_path, card_id))
            self.connection.commit()
        except Error as e:
            print(e)

    def update_image_by_id(self, card_id, image_path):
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                UPDATE cards SET Image = ? WHERE ID = ?
            ''', (image_path, card_id))
            self.connection.commit()
        except Error as e:
            print(e)

    def get_all_cards(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                SELECT * FROM cards
            ''')
            return cursor.fetchall()
        except Error as e:
            print(e)

    def save_blobs_to_files(self, card_id, save_path):
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                SELECT SoundVocabulary, SoundMeaning, SoundExample, Image FROM cards WHERE ID = ?
            ''', (card_id,))
            result = cursor.fetchone()
            if result:
                sound_vocabulary_blob, sound_meaning_blob, sound_example_blob, image_blob = result
                with open(os.path.join(save_path, f"{card_id}_sound_vocabulary.mp3"), "wb") as f:
                    f.write(sound_vocabulary_blob)
                with open(os.path.join(save_path, f"{card_id}_sound_meaning.mp3"), "wb") as f:
                    f.write(sound_meaning_blob)
                with open(os.path.join(save_path, f"{card_id}_sound_example.mp3"), "wb") as f:
                    f.write(sound_example_blob)
                with open(os.path.join(save_path, f"{card_id}_image.jpg"), "wb") as f:
                    f.write(image_blob)
                print(f"Files saved successfully to {save_path}")
            else:
                print("Card not found with given ID.")
        except Error as e:
            print(e)

    def close(self):
        if self.connection:
            self.connection.close()


if __name__ == "__main__":
    db_file = "cards.db"
    db_helper = CardDBHelper(db_file)

    # 插入一条示例数据，其中 SoundVocabulary、SoundMeaning、SoundExample 和 Image 为空
    example_card = (
        "Example Vocabulary",
        "Example Pronunciation",
        "Example Part of Speech",
        "Example Forms",
        "Example Meaning",
        "Example Example",
        "Example Chinese Example",
        None,
        None,
        None,
        None
    )
    db_helper.insert_card(example_card)

    # 示例: 通过 Vocabulary 和 Example 获取卡片 ID
    card_id = db_helper.get_card_id_by_vocabulary_and_example(
        "Example Vocabulary", "Example Example")
    print("Card ID:", card_id)

    # 示例: 更新卡片的声音文件内容
    with open("/path/to/sound_vocabulary.mp3", "rb") as f:
        sound_vocabulary_data = f.read()
    with open("/path/to/sound_meaning.mp3", "rb") as f:
        sound_meaning_data = f.read()
    with open("/path/to/sound_example.mp3", "rb") as f:
        sound_example_data = f.read()
    db_helper.update_sound_files_by_id(
        card_id, sound_vocabulary_data, sound_meaning_data, sound_example_data)

    # 示例: 更新卡片的图像内容
    with open("/path/to/image.jpg", "rb") as f:
        image_data = f.read()
    db_helper.update_image_by_id(card_id, image_data)

    db_helper.close_connection()
