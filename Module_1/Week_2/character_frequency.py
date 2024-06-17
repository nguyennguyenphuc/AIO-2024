def character_count(word):
    character_statistic = {}
    for char in word:
        if char in character_statistic:
            character_statistic[char] += 1
        else:
            character_statistic[char] = 1
    return character_statistic


def main():
    assert character_count("Happiness") == {
        'H': 1, 'a': 1, 'p': 2, 'i': 1, 'n': 1, 'e': 1, 's': 2}
    assert character_count("smiles") == {
        's': 2, 'm': 1, 'i': 1, 'l': 1, 'e': 1}


if __name__ == "__main__":
    main()
