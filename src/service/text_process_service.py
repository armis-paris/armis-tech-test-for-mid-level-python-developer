def _append_if_not_exist(char: str, current_list: list) -> list:
    """
    I created this function instead of using a set() object to order the list by the first
    position in the original string.
    """
    if char not in current_list:
        current_list.append(char)
    return current_list


class TextProcessService:

    def extract_information(self, text: str) -> dict:
        try:
            number_of_words: int = len(text.split())
            length_of_text: int = len(text)

            unique_alphabetic_characters = []
            unique_numerical_characters = []
            unique_other_characters = []

            for character in text:
                if character.isalpha():
                    _append_if_not_exist(character, unique_alphabetic_characters)
                elif character.isnumeric():
                    _append_if_not_exist(character, unique_numerical_characters)
                else:
                    _append_if_not_exist(character, unique_other_characters)

            return {
                'number_of_words': number_of_words,
                'length_of_text': length_of_text,
                'unique_alphabetic_characters': unique_alphabetic_characters,
                'unique_numerical_characters': unique_numerical_characters,
                'unique_other_characters': unique_other_characters
            }
        except Exception as e:
            raise Exception(f"Error while processing text: {e}")
