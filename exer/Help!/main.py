import random
import sys
from random import randrange

def add_word():
    words = ["ja", "nej", "hej", "bla", "any" , "thing", "how", "now", "brown", "now","cow", "who", "are", "you"]
    return words[random.randint(0,13)]
def add_char():
    char = ["a", "b", "c", "d", "e", "f", "r", "t", "m", "x"]
    return char[random.randint(0,9)]

def word(b):
    w = ""
    if b == 1:
        w = add_word()
    if b == 0:
        w = "<" + add_char() + ">"
    return w

def testing():
    A =[]
    B = []
    aw = ""
    bw = ""
    n = random.randint(1,5)
    m = random.randint(1,4)
    for i in range(n):
        for j in range(m):
            aw += word(random.randint(0,1)) + " "
            bw += word(random.randint(0,1)) + " "
        A.append(aw)
        B.append(bw)
    return A, B, n

def fill_sets():
    import sys

    A = []
    B = []
    n = int(sys.stdin.readline())

    for i in range(n * 2):
        row = sys.stdin.readline().split()
        if not i % 2 == 0:
            A.append(row)
        else:
            B.append(row)
    return A, B, n

def fill_txt(file):
    A = []
    B = []
    with open(file) as f:
        lines = f.readlines()

    n = int(lines[0])

    for i in range(n * 2 + 1):
        if not i % 2 == 0:
            A.append(lines[i].split())
        else:
            B.append(lines[i].split())
    B.pop(0)
    return A, B, n


def is_word(word):
    return "<" and ">" not in word

def rest_of_list(p,s,index,H):
    i= index
    while i+1 < len(p):
        if p[index] == p[i+1]:
            if is_word(s[i+1]):
                H[p[index]] = s[i+1]
                return True
        i += 1
    return False

def add_phrase(primary,secondary,index, Hmap):
    phrase = ""
    # if a is a word
    if is_word(primary[index]):
        # we add it to the phrase
        phrase += primary[index] + " "
    else:
        #primary is a placeholder already in Hmap,
        if Hmap.get(primary[index]) != None:
            #add the word
            phrase += Hmap.get(primary[index]) + " "

        #primary is a placeholder but not added i hmap
        else:
            #secondary is a word
            if is_word(secondary[index]):
                # is secondary "any"
                #add to hmap and add phrase
                Hmap[primary[index]] = secondary[index]
                phrase += Hmap.get(primary[index]) + " "
            #secondary is also a phrase

            else:
                #linear search for other equal place holder and
                # see if word in secondary there
                #gets an updated key:val if true
                T = rest_of_list(primary,secondary,index,Hmap)
                if(T):
                    #if true we add the phrase
                    phrase += Hmap.get(primary[index])
                else:
                    #if not we add its placeholder
                    phrase += primary[index]
    return phrase

def cleanup(t_a, t_b, size):

    for i in range(size):
        if "<" in t_a[i] and "<" not in t_b[i]:
            t_a[i] = t_b[i]
        if "<" in t_b[i] and "<" not in t_a[i]:
            t_b[i] = t_a[i]
        if "<" in t_b[i] and "<" in t_a[i]:
            t_a[i] = "any"
            t_b[i] = "any"

    return t_a, t_b

def fill(a,b,size,H):
    phrase = ""
    for i in range(size):
        phrase += add_phrase(a, b, i, H) + " "
    return phrase

def solve(a, b):
    Hmap_a = {}
    Hmap_b = {}

    if not len(a) == len(b):
        return "-"
    size = len(a)
    for i in range(size):
        a = fill(a, b, size, Hmap_a).split()
        b = fill(b, a, size, Hmap_b).split()

    Hmap_b.clear()
    Hmap_a.clear()
    a = fill(a, b, size, Hmap_a).split()
    b = fill(b, a, size, Hmap_b).split()

    a,b = cleanup(a,b,size)

    if a == b:
        phrase_a = " "
        return phrase_a.join(a)
    else:
        return "-"

##### from .txt
file = "test.txt"
A = []
B = []
ans = ""
n = int

#A, B, n = testing()

#A, B, n = fill_txt(file)

A, B, n = fill_sets()
#####
#test = testing()
#test = testing()
#print(test)

for i in range(n):
    ans = solve(A[i], B[i])
    print(ans)



