def main():
    filepath = "books/frankenstein.txt"
    text = get_text(filepath)
    words = word_count(text)
    print(f"--- Begin report of books {filepath} ---")
    print(f"{words} words found in Document\n\n")
    # print(character_count(text.lower()))
    sorted_dict = (sort_dict(character_count(text.lower())))

    for char, count in sorted_dict:
        print(f"The {char} character appears {count} times in the text.")
    
    print("--- End report ---")


    
def get_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def character_count(text):
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            if char.isalpha():
                char_count[char] = 1
    return char_count


def word_count(text):
    words = text.split()
    return len(words)

def sort_dict(dict):
    list_from_dict = list(dict.items())
    list_from_dict.sort(reverse=True, key=lambda x: x[1])
    return list_from_dict


main()
