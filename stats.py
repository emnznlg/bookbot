def print_num_words(text):
    word_array = text.split()
    num_words = len(word_array)
    print(f"Found {num_words} total words")

def get_num_chars(text):
    char_count = {}

    for char in text.lower():
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    
    return char_count

def print_sorted_list(dict_of_chars):
    list_of_chars = list(dict_of_chars.items())
    list_of_chars.sort(reverse=True, key=sort_on)
    for item in list_of_chars:
        if item[0].isalpha():
            print(f"{item[0]}: {item[1]}")

def sort_on(item):
    return item[1]