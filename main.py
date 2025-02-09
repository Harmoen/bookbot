def main() -> None:
    generate_report("books/frankenstein.txt")

    return 


def generate_report(path_to_file : str) -> None:
    file_text = file_to_string(path_to_file)

    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count(file_text)} words found in document")
    print("")

    # Sorting the letters in 
    alphabet = "abcdefghijklmnopqrztuvwxyz"
    letter_counts = character_counts(file_text)

    for letter in alphabet:
        if letter in letter_counts.keys():
            print(f"The '{letter}' was found {letter_counts[letter]} times ")
        

    print("--- End report ---")

    return



def file_to_string(path_to_file : str) -> str:
    with open(path_to_file) as file:
        file_contents = file.read()
        return file_contents


def word_count(text : str) -> int:
    return len(text.split())


def character_counts(text : str) -> dict:
    characters = {}

    for character in text.lower():
        if character in characters.keys():
            characters[character] += 1
        else:
            characters[character] = 1
    
    return characters


# Call Main to start programe
main()