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
