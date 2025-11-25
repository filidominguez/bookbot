def get_num_words(text):
    words = text.split()
    return len(words)



def character_count(text):
    count = {}
    for ch in text.lower():
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
    return count



def sort_on(item):
    return item["num"]

def sort_char(count_dict):
    results = []
    for ch, n in count_dict.items():
        if ch.isalpha():
            results.append({"char": ch, "num": n})
    results.sort(key=sort_on, reverse=True)
    return results

    