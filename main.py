def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        count_words(file_contents)
        count_letters(file_contents)

def count_words(contents):
    words = contents.split()
    count = len(words)
    print(f"{count} words were found in the document.\n")

def count_letters(contents):
    count = 0
    unique = {}
    alpha = "abcdefghijklmnopqrstuvwxyz"
    loweredstr = contents.lower()
    for i in loweredstr:
        if i in alpha:
            unique[i] = unique.get(i,count) + 1
    for w in unique:
        print(f"The {w} character was found {unique[w]} times.")




main()