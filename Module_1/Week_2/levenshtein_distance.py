def levenshtein_distance(token1, token2):
    m, n = len(token1), len(token2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if token1[i - 1] == token2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,    # Deletion
                               dp[i][j - 1] + 1,    # Insertion
                               dp[i - 1][j - 1] + 1)  # Substitution

    return dp[m][n]


def main():
    assert levenshtein_distance("kitten", "sitting") == 3
    assert levenshtein_distance("hi", "hello") == 4
    assert levenshtein_distance("hola", "hello") == 3


if __name__ == "__main__":
    main()
