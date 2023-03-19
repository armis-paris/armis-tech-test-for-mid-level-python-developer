from dataclasses import dataclass


@dataclass
class TextExtractedInformation:
    number_of_words: int
    length_of_text: int
    unique_alphabetic_characters: set
    unique_numerical_characters: set
    unique_other_characters: set


class TextProcessService:
    def __init__(self, text: str):
        if not isinstance(text, str):
            # That can be enhanced by using a library for type enforcement like pydantic
            raise Exception("Text must be a string")

        # choose to save the text as private without any setter to avoid to change it.
        self.__text = text

        # Choose to save the base information in the object so to avoid to recompute it.
        self.__length_of_text = len(text)
        self.__number_of_words = len(text.split())

    """
    Even thought this implementation and previous one have the same O(n) complexity,
    I chose to use multiple functions to enhance readability, and adhere to the single responsibility principle.
    That can be enhanced in case of complicated logic to different classes that we can inject.
    """

    def __get_unique_alphabetic_characters(self) -> set:
        return {char for char in self.__text if char.isalpha()}

    def __get_unique_numerical_characters(self) -> set:
        return {char for char in self.__text if char.isnumeric()}

    def __get_unique_other_characters(self) -> set:
        return {
            char for char in self.__text if not char.isalpha() and not char.isnumeric()
        }

    def extract_information(self) -> TextExtractedInformation:

        return TextExtractedInformation(
            number_of_words=self.__number_of_words,
            length_of_text=self.__length_of_text,
            unique_alphabetic_characters=self.__get_unique_alphabetic_characters(),
            unique_numerical_characters=self.__get_unique_numerical_characters(),
            unique_other_characters=self.__get_unique_other_characters(),
        )
