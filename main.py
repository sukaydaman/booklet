from stats import get_book_text
from stats import get_num_letters
from stats import get_num_words
from stats import sorted_dict

import sys

def main():
	try:
		book_path = sys.argv[1]
		total_words = get_num_words(get_book_text(book_path))
		print("============ BOOKBOT ============")
		print(f"Analyzing book found at {book_path}")
		print("----------- Word Count ----------")
		print(f"Found {total_words} total words")
		print("--------- Character Count -------")
		sorted_dict(get_num_letters(get_book_text(book_path)))
		print("============= END ===============")
	except IndexError:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	return
main()
