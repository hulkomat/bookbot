from stats import get_word_count
from stats import get_character_count

def get_book_text(filepath: str):
    with open(filepath) as f:
        return f.read()
    

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    # print(book_text)
    num_words = get_word_count(book_text)
    character_dictionary = get_character_count(book_text)
    print(f"{num_words} words found in the document")
    print(character_dictionary)

main()
