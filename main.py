def count_words(string):
    words_array = string.split()
    return len(words_array)

def sort_on(dict):
    return dict["repeats"]

def get_letters(string):
    valid_letters = 'abcdefghijklmnopqrstuvwxyz'
    counter = {}
    as_list = []
    for character in string:
        if character.lower() in valid_letters and character.lower() in counter:
            counter[character.lower()] += 1
        elif character.lower() in valid_letters:
            counter[character.lower()] = 1
    for element in counter:
        as_list.append({"letter": element, "repeats": counter[element]})

    as_list.sort(reverse=True, key=sort_on)
    return as_list

def main():
    with open("books/frankestein.txt") as f:
        file_contents = f.read()
        number_of_words = count_words(file_contents)
        letters = get_letters(file_contents)

        print("Printing report for books/frankestein.txt")
        print(f"The book contains {number_of_words} words.")
        for i in range(0, len(letters)):
            print(f"The letter '{letters[i]['letter']}' was found {letters[i]['repeats']} times.")
        print("End of report")

main()
