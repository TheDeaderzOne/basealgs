def KMP(string):
    n = len(string)
    kmparr = [0] * n
    for i in range(1, n):
        j = kmparr[i - 1]
        while j > 0 and string[i] != string[j]:
            j = kmparr[j - 1]
        if string[i] == string[j]:
            j += 1
        kmparr[i] = j
    return kmparr


def kmppatternmatcher(string, pattern):
    arr = []
    kmparr = KMP(pattern)
    i = 0
    j = 0
    if pattern == "":
        return []
    while i < len(string):
        if j == len(pattern):
            arr.append(i - len(pattern))
            j = kmparr[j - 1]
        elif string[i] == pattern[j]:
            i += 1
            j += 1
        else:
            while j > 0 and string[i] != string[j]:
                j = kmparr[j - 1]
            i += 1
    if j == len(pattern):
        arr.append(i - len(pattern))
    return arr


print(kmppatternmatcher("ABABA", "ABA"))
print(kmppatternmatcher("AABAACAADAABAAABAA", "AABA"))
print(kmppatternmatcher("AAAA", "AA"))
print(kmppatternmatcher("AAA", "A"))
print(kmppatternmatcher("ABCDE", "ABCDE"))
print(kmppatternmatcher("ABABABABAB", "ABAB"))
print(kmppatternmatcher("AABABCABCDABCDABCDABCD", "ABCD"))
print(kmppatternmatcher("ABCDEFGHI", "XYZ"))
print(kmppatternmatcher("ABC", "ABCD"))
print(kmppatternmatcher("HELLOWORLD", ""))
print(kmppatternmatcher("", "ABC"))
print(KMP("ACBACDACBACBACDA"))
print(KMP("ATT#HATTIVATTI"))
