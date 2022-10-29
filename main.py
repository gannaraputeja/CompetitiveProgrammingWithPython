# This is a sample Python script.
#from fractions import Fraction
import bisect
from collections import defaultdict
from collections import Counter
import sys

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    for i in range(0, 14, 1):
        print(f'Hi, {i}')  # Press ⌘F8 to toggle the breakpoint.
        yield (i,)

def my_print():
    a = print_hi('PyCharm')
    print(type(a))
    for x in a:
        print(x)

def fraction():
    f = 3/2
    # f: Fraction = 3/2
    print(str(f))
    f = 5/2
    print(f)

def _list_():
    a = [0 * 10 for _ in range(10)]
    print(a)
    li = [5, 7, 9, 1, 3]
    print(li)
    print(li[:])
    print(bisect.bisect(sorted(li), 4))
    l2 = sorted(li[:])
    bisect.insort(l2, 4)
    print(l2)

def counter_():
    c = Counter()
    print(c)
    c['a'] += 2
    print(c)

def dict_():
    d = {}
    print(d)
    d['a'] = []
    d['a'].append(1)
    print(d)
    d1 = defaultdict(list)
    d1['a'].append(1)
    print(d1)

def lists():
    m = [[0] * 10] * 10 # Do not write this
    print(m)
    M1 = [[0] * 10 for _ in range(10)]
    print(M1)
    M2 = [i for i in range(10, -1, -1)]
    print(M2)

def read_stdin():
    height, width = map(int, sys.stdin.readline().split())
    print(height, width)

def min_diff_in_arr():
    l = [85, 10, 23, 47, 32, 58, 1, 16, 78]
    l.sort()
    min_val, min_index = min((l[i]-l[i-1], i) for i in range(1, len(l)))
    print(min_val, l[min_index-1], l[min_index])

def max_interval_intersec():
    S = [(1,4),(3,6),(5,9)]
    B = ([(left, +1) for left, right in S] + [(right, -1) for left, right in S])
    B.sort()
    print(B)
    c=0
    best = (c, None)
    for x, d in B:
        c += d
        if best[0] < c:
            best = (c, x)
    print(best)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    max_interval_intersec()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
