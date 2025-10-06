def get_total_words(book_content):
    content_arr = book_content.split()
    return len(content_arr)

def get_char_count(book_content):
    char_dict = {}
    char_list = list(book_content.lower())
    
    for char in char_list:
        char_dict[char] = char_dict.get(char, 0) + 1

    return char_dict

def sort_on(d):
    return d["num"]

def sorted_dict(char_dict):
    sorted_list = []

    for char, count in char_dict.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})

    sorted_list.sort(key=sort_on, reverse=True)  # Sort descending
    return sorted_list