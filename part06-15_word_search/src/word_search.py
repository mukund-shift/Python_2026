# Very useful program

def blank_indices(search_term: str):
    indices = []
    for i in range(len(search_term)):
        if search_term[i] == ".":
            indices.append(i)
    return indices


def find_words(search_term: str):
    with open("words.txt") as words:
        all_words = set()
        for line in words:
            line = line.strip()
            all_words.add(line)

    found = set()
    if "*" not in search_term and "." not in search_term:
        if search_term not in all_words:
            return []
        found.add(search_term)                              #term = word
        return list(found)
    
    elif "*" in search_term:
        if search_term[0] == "*" and search_term[-1] != "*":            # term is suffix
            for word in all_words:
                if word.endswith(search_term[1:]):
                    found.add(word)
        elif search_term[0] != "*" and search_term[-1] == "*":            # term is prefix
            for word in all_words:
                if word.startswith(search_term[:-1]):
                    found.add(word)
        else:
            for word in all_words:
                if search_term[1:-1] in word:
                    found.add(word)                   # word contains term,no dupes due to sets
        found = sorted(list(found))
        return found

    else:
        indices = blank_indices(search_term)
        for word in all_words:
            if len(word) != len(search_term):
                continue
            valid = True
            for i in range(len(word)):
                if i not in indices and word[i] != search_term[i]:
                    valid = False
            if valid:
                found.add(word)
        found = sorted(list(found))
        return found


if __name__ == "__main__":
    found = find_words("*vokes")
    print(found)
    print("======================================================")

    
