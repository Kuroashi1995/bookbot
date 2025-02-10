def count_words(string):
    words_array = string.split()
    return len(words_array)

def get_characters(string):
    unique_chars = set()
    counter = {}
    for character in string:
        if character.lower() in unique_chars:
            counter[character.lower()] += 1
        else:
            unique_chars.add(character.lower())
            counter[character.lower()] = 1
    return counter

def main():
    with open("books/frankestein.txt") as f:
        file_contents = f.read()
        number_of_words = count_words(file_contents)
        characters = get_characters(file_contents)
        print(characters)

main()
