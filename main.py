from stats import count_words, count_unique_symbols, sorted_symbols_count

import sys


def get_book_text(filename):
    with open(filename) as f:
        return f.read()
    
def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    book_text = get_book_text(filename)
    print(f"Found {count_words(book_text)} total words")
    print("--------------------------------")
    print("Unique symbols found in the document")
    print("--------------------------------")
    symbols = count_unique_symbols(book_text)
    sorted_symbols = sorted_symbols_count(symbols)
    for symbol in sorted_symbols:
        print(f"{symbol['symbol']}: {symbol['count']}")
    print("--------------------------------")
main()