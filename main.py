def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    chars_sorted = chars_sorted_list(char_count)

    print(f"{num_words} words found")
    print()

    for item in chars_sorted:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']} character was found {item['num']} times")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_char_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] +=1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]

def chars_sorted_list(num_chars):
    sorted_list = []
    for ch in num_chars:
        sorted_list.append({"char": ch, "num": num_chars[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()