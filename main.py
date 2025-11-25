import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]



from stats import get_num_words, character_count, sort_char



def get_book_text(books):
    with open(books) as f:
        text = f.read()
    return text



def main():
    read = get_book_text(book_path)
    char = character_count(read)
    sorted_chars = sort_char(char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count -----------")
    print(f"Found {get_num_words(read)} total words")
    print("--------- Character Count ---------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END =============")


   
    


main()

