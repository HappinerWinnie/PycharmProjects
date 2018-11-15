'''
def song_decoder(song):
    song.replace('WUB',' ')
    return song

print(song_decoder('WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB'))
'''

#song = 'WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB'
# s = ' '.join(song.replace('WUB', ' ').split())
#s = ' '.join(song.replace('WUB', ' ').split())
#print(song.lower())

# L = []
# def alphabet_position(text):
#     t = list(text.lower())
#     l = len(t)
#     for i in range(l):
#         if 'a' <= t[i] <= 'z':
#             L.append(ord(t[i]))
#     return L
#
# print(alphabet_position("The sunset sets at twelve o' clock."))

'''
def alphabet_position(text):
	ans = ''
	inp = list('abcdefghijklmnopqrstuvwxyz')
	for i in text:
		if i.isalpha():
			ans += str(inp.index(i.lower()) + 1) + ' '
	return ans[0:len(ans)-1]

print(alphabet_position("The sunset sets at twelve o' clock."))


def alphabet_pos(text):
    L = []
    t = list(text.lower())
    l = len(t)
    for i in range(l):
        if t[i].isalpha and 'a' <= t[i] <='z':
            #print(type(str(ord(t[i])-ord('a') + 1)))
            L.append(str(ord(t[i])-ord('a') + 1))
    return str(' '.join(L))

print(alphabet_pos("The sunset sets at twelve o' clock."))

def alphabet_p(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
print(alphabet_p("The sunset sets at twelve o' clock."))

import re
def alphabet_po(text):
    return ' '.join(map(lambda x: str(ord(x) - 96), re.sub('(?i)[^a-z]', '', text.lower())))
print(alphabet_po("The sunset sets at twelve o' clock."))
'''

# def duplicate_count(text):
#     count_num = 0
#     s = ' '
#     # Your code goes here
#     for i in text:
#         if (text.count(i) >= 2) and (s.find(i)==0):
#             count_num += 1
#             s += i
#         else:
#             continue
#     return count_num
# print(duplicate_count('aabbcde'))

'''
from collections import Counter

def duplicate_count(text):
    duplicates = 0

    for key, value in Counter(list(text.lower())).items():
        if value > 1:
            duplicates += 1

    return duplicates
print(duplicate_count('helloppd'))

import re 

def duplicate_count(text):

    lower_text=text.lower()
    duplicates=set()

    for c in lower_text:
        if len(re.findall(c, lower_text)) > 1:
            duplicates.add(c)
    return len(duplicates)
'''


def longest_consec(strarr, k):
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ''

    longest = index = 0
    for i in range(n - k + 1):
        length = sum([len(s) for s in strarr[i: i + k]])
        print([len(s) for s in strarr[i: i + k]])
        print(length)
        if length > longest:
            longest = length
            index = i

    return ''.join(strarr[index: index + k])


print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2))

