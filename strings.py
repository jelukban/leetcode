# 830. Positions of Large Groups
def largeGroupPositions(s):
    large_groups = []
    pair = []

    for i in range(0, len(s)):

        if (i == len(s)-1) and (s[i] == s[i-1] and pair != []):
            pair.append(i)
        elif i == len(s) - 1:
            continue
        elif (s[i] == s[i+1]) and (i == 0):
            pair.append(i)
        elif (s[i] == s[i+1]) and (s[i] == s[i-1]):
            continue
        elif s[i] == s[i+1]:
            pair.append(i)
        elif s[i] == s[i-1] and pair != []:
            pair.append(i)

        if len(pair) == 2 and ((pair[1] - pair[0] + 1) >= 3):
            large_groups.append(pair)
            pair = []
        elif len(pair) == 2:
            pair = []

    return large_groups

    # A cleaner, preferred way


def largeGroupPositionsAlternative(s):
    large_groups = []
    start = 0

    for i in range(len(s)):
        if (i == len(s)-1) or (s[i] != s[i+1]):
            if i - start + 1 >= 3:
                large_groups.append([start, i])
            start = i+1
    return large_groups

# 242. Valid Anagram


def isAnagram(s, t):
    s_lst = list(s)
    t_lst = list(t)

    s_lst.sort()
    t_lst.sort()

    return s_lst == t_lst


# 225. Valid Palindrome
def isPalindrome(s):
    s_list = []

    for char in s.lower():
        if char in 'abcdefghijklmnopqrstuvwxyz0123456789':
            s_list.append(char)

    return s_list == s_list[::-1]
