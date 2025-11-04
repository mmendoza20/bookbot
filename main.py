import sys
from stats import get_word_count, get_letter_count, sort_letters

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

def get_book_text(book):
	with open(book) as f:
		file_contents = f.read()
	return file_contents

def main():
	book_location = sys.argv[1]
	book_text = get_book_text(book_location)
	num_words = get_word_count(book_location)
	num_letters = get_letter_count(book_location)
	char_sort = sort_letters(num_letters)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_location}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for item in char_sort:
		letter =  item['char']
		count = item['num']
		if letter.isalpha():
			print(f"{letter}: {count}")

main()
