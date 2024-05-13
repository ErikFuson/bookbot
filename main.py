def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        count_words(file_contents)

def count_words(contents):
    words = contents.split()
    count = len(words)
    print(count)

main()