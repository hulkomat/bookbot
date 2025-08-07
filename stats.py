def get_word_count(text: str) -> int:
    return len(text.split())

def get_character_count(text: str) -> dict:
    res_dictionary: dict = {}
    for char in text.lower():
        if char not in res_dictionary:
            res_dictionary[char] = 0
        res_dictionary[char] += 1
    return res_dictionary

def sort_on_num(item: dict) -> int:
    return item["num"]

def sorted_dict_by_count(dictionary: dict) -> list:
    unsorted_list = []
    for char, count in dictionary.items():
        item_dict = { "char" : char, "num" : count }
        unsorted_list.append(item_dict)
    return sorted(unsorted_list, key=sort_on_num, reverse=True)