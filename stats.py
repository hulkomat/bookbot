def get_word_count(text: str):
    return len(text.split())

def get_character_count(text: str):
    res_dictionary: dict = {}
    for char in text.lower():
        if char not in res_dictionary:
            res_dictionary[char] = 0
        res_dictionary[char] += 1
    return res_dictionary