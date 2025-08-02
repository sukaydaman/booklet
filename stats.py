def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents

def get_num_letters(file_contents):
	sum_of_letters = {}
	words_total = file_contents.split()
	for words in words_total:
		for letter in words:
			base_letter = letter.lower() 
			if base_letter in sum_of_letters:
				sum_of_letters[base_letter] += 1
			else: sum_of_letters[base_letter] = 1
	return sum_of_letters

def get_num_words(file_contents):
	return len(file_contents.split())

def sorted_dict(dict):
	results = []
	for char, num in dict.items():
    		new_dict = {"char": char, "num": num}
    		results.append(new_dict)
	for item in results:
    		print(f"{item['char']}: {item['num']}")
	return 

