def count_words(text):
    return len(text.split())
    
def count_unique_symbols(text: str):
     unique_symbols = {}
     for char in text:
         if char.isalpha():
             char = char.lower()
             if char in unique_symbols:
                 unique_symbols[char] += 1
             else:
                 unique_symbols[char] = 1
     return unique_symbols

def sort_on_count(items):
    return items["count"]

def sorted_symbols_count(symbols: dict):
    arr = []
    for symbol in sorted(symbols):
        arr.append({"symbol": symbol, "count": symbols[symbol]})
    arr.sort(key=sort_on_count, reverse=True)
    return arr