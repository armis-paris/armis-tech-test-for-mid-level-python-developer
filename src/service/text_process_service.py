class TextProcessService:

    def extract_information(self, text: str) -> dict:
        number_of_words: int = len(text.split())
        length_of_text: int = len(text)

        unique_alphabetic_characters = []
        unique_numerical_characters = []
        unique_other_characters = []

        for character in text:
            if character.isalpha():
                unique_alphabetic_characters.append(character)
            if character.isnumeric():
                unique_numerical_characters.append(character)
            unique_other_characters.append(character)

        return {'number_of_words': number_of_words,
                'length_of_text': length_of_text,
                'unique_alphabhetic_characters': unique_alphabetic_characters,
                'unique_numerical_characters': unique_numerical_characters,
                'unique_other_characters': unique_other_characters}
