
"""def main():
    with open("/home/jeemiller/workspace/github.com/JeeMill/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()

    word_count = len(file_contents.split())
    print(word_count)"""

def main():
    book_path = "/home/jeemiller/workspace/github.com/JeeMill/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = get_letter_count(text)
    Alpha_list = get_dict_list(letter_count)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document", '\n')
    report = get_report(Alpha_list)


def get_report(list):
    for i in list:
        print(f"The '{i['name']}' character was found {i['count']} times")
    print("--- End report ---")

def get_dict_list(dict):
    # reformat dictionary to list of dictionaries [{letter, Count}]
    a_list = []
    
    for i in dict:
        new_dict = {}
        new_dict["name"] = i
        new_dict["count"] = dict[i]
        a_list.append(new_dict)
    
    return a_list
    

def get_letter_count(text):
    Alpha = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 
             'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 
             's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
    
    for t in text:
        if t.lower() in Alpha:
            t = t.lower()
            Alpha[t] += 1

    return Alpha

def get_num_words(text):
    words = text.split()
    return len(words)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()