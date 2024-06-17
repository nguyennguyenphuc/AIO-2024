def count_word(file_path):
    counter = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.strip().lower().split()
            for word in words:
                if word in counter:
                    counter[word] += 1
                else:
                    counter[word] = 1
    return counter


def main():
    file_path = 'P1_data.txt'
    result = count_word(file_path)
    assert result.get('who', 0) == 3
    assert result.get('man', 0) == 4


if __name__ == "__main__":
    main()
