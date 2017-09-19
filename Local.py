import sys

def qsort_words(w, n, first, last):
    '''
        Realization of quick sort algoritm for dictionary.
        w -- array of words
        n -- array of frequencies
        first, last -- the first and the last bounds of an arrays' parts that
        are being sorted on the current iteration

    '''
    l = first
    r = last
    m = n[int(((l+r)/2))]

    while l <= r:
        while n[l] > m:
            l += 1
        while n[r] < m:
            r -= 1

        if l <= r:
            if l < r:
                n[l], n[r] = n[r], n[l]
                w[l], w[r] = w[r], w[l]
            l += 1
            r -= 1

    if l < last:
        qsort_words(w,n,l,last)
    if r > first:
        qsort_words(w,n,first,r)

try:
    n = int(input())
except:
    print('n must be a positive integer with base 10')
    sys.exit()

wi = []
ni = []

for i in range(0,n):
    s = input().split()
    if len(s) != 2:
        continue
    wi.append(s[0])
    try:
        ni.append(int(s[1]))
    except:
        wi.pop() # ignore a word if second argument is not int

if len(wi) == 0:
    print('Error: dictionary is empty')
    sys.exit()

qsort_words(wi,ni,0,len(wi)-1)

for i in range(0,len(ni)): # Sorting words with same frequency.
    if ni[i] == ni[i-1]:
        t = i
        while True:
            if t < len(ni):
                if ni[t] == ni[t-1]:
                    t += 1
                else:
                    break
            else:
                break
        wi[i-1:t+1] = sorted(wi[i-1:t+1])

m = int(input())

ui = []

for i in range(0,m):
    request = input()
    if len(request) ==0 or ' ' in request:
        continue
    ui.append(request)

for user_word in ui: # Finding words in sorted dictionary
    answers = list(filter(lambda s: s.startswith(user_word),wi))
    if len(answers) > 10:
        answers = answers[0:10]
    if len(answers) > 0:
        for ans in answers:
            print(ans)
        print()