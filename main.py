from stats import get_word_count, sorted_dict_by_count
from stats import get_character_count

def get_book_text(filepath: str):
    with open(filepath) as f:
        return f.read()
    

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    # print(book_text)
    num_words = get_word_count(book_text)
    character_dictionary = get_character_count(book_text)
    sorted_list = sorted_dict_by_count(character_dictionary)

    print(f"============ BOOKBOT ============\n"
          f"Analyzing book found at books/frankenstein.txt...\n"
          f"----------- Word Count ----------\n"
          f"Found {num_words} total words\n"
          f"--------- Character Count -------")
    for item in sorted_list:
        if not item['char'].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============\n")

main()
