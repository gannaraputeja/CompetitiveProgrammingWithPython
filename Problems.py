import sys


# Input Test - https://www.spoj.com/problems/INTEST/
def intest():
    n, k = (map(int, sys.stdin.readline().split()))
    narr = [int(sys.stdin.readline()) for _ in range(n)]
    # c = 0
    # for i in range(len(narr)):
    #     if narr[i] % k == 0:
    #         c+=1
    c = sum(list(map(lambda x: x%k == 0, narr)))
    print(c)


# Cencry Encryption - https://www.spoj.com/problems/CENCRY/
def cencry_encryption():
    n = int(sys.stdin.readline())
    msgs = [sys.stdin.readline().strip() for _ in range(n)]
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    result = []
    for str in msgs:
        strcount = {}
        estr = []
        for c in str:
            if c in strcount:
                strcount[c] += 1
            else:
                strcount[c] = 1
            ec = ''
            if c in vowels:
                ec = consonants[((strcount[c]-1)*len(vowels) + vowels.index(c))%len(consonants)]
            else:
                ec = vowels[((strcount[c]-1)*len(consonants) + consonants.index(c))%len(vowels)]
            estr.append(ec)
        result.append("".join(estr))
    for str in result:
        print(str)


# Phonelist - https://www.spoj.com/problems/PHONELST/
def phonelist():
    key = "911"
    result = []
    t = int(sys.stdin.readline())
    for i in range(t):
        n = int(sys.stdin.readline())
        lines = [sys.stdin.readline().strip() for _ in range(n)]
        if sum(map(lambda line: int(line.startswith(key)), lines)) > 0:
            result.append("Yes")
        else:
            result.append("No")
    [print(x) for x in result]


# Back to the Future - https://prologin.org/train/2012/semifinal/retour_vers_le_futur
def back_to_future():
    # n = int(sys.stdin.readline())
    # print(n)
    # l = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    # print(l)
    l = [(1, 4), (3, 6), (5, 9)]
    occurences = [(left, 1) for left, right in l] + [(right, -1) for left, right in l]
    occurences.sort()
    counter = 0
    result = (counter, None)
    for time, period in occurences:
        counter += period
        if result[0] < counter:
            result = (counter, time)
    print(result[0])


# A Concrete Simulation - https://www.spoj.com/problems/ACS/
def acs():
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

