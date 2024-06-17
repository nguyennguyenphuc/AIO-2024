def max_kernel(num_list, k):
    if not num_list or k == 0:
        return []

    result = []
    for i in range(len(num_list) - k + 1):
        window = num_list[i:i + k]
        result.append(max(window))
    return result


def main():
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 3
    assert max_kernel(num_list, k) == [5, 5, 5, 5, 10, 12, 33, 33]


if __name__ == "__main__":
    main()
