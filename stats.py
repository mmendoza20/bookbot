def get_word_count(book):
        with open(book) as f:
                file_contents = f.read()
        return len(file_contents.split())

def get_letter_count(book):
	letter_counts = {}
	with open(book) as f:
		file_contents =  f.read()
	for char in file_contents:
		letter_counts[char.lower()] = letter_counts.get(char.lower(), 0) + 1
	return letter_counts

def sort_letters(letters):
	def sort_on(items):
		return items["num"]

	sorted_letters = [
		{'char': key, 'num': value}
		for key, value in letters.items()
	]
	sorted_letters.sort(reverse=True, key=sort_on)
	return sorted_letters
