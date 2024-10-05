def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_dict_chars(text)
    print(f"{num_words} words found in the document")
    print("")
    print(chars_dict)

# get the number of words in the text
def get_num_words(text):
    words = text.split()
    return len(words)

# this function is called by chars_dict_to_sorted_list when it sorts the list,
# this helps tell the sort to go by the "num" associated with each char from highest to lowest.
def sort_on(d):
    return d["num"]

# Here we are creating a list for each char in the dict of nums and chars.
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

# create a dict with chars that appear in the text and how many times they appear
def get_dict_chars(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] +=1
        else:
            chars[lowered] = 1
    return chars

# get the text from the specified file path
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()
