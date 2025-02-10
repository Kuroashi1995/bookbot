def count_words(string):
    words_array = string.split()
    return len(words_array)


def main():
    with open("books/frankestein.txt") as f:
        file_contents = f.read()
        number_of_words = count_words(file_contents)
        print(number_of_words)

main()
