"""
666
1666, 2666, 3666, 4666, 5666, 
6660, 6661, 6662, 6663, 6664, 6665, 6666, 6667, 6668, 6669
7666, 8666, 9666, 
10666, 11666 12666 13666 14666 15666 
16660 16660 16661 16662 16663 16664 16665 16666 16667 16668 16669
17666 18666 19666 
20666 21666 22666 23666 24666 25666
27666 28666 29666
26661 26662 26663 26663 26664 26665 26666 26667 26668 26669

완전탐색
"""

n = int(input())

titles = [666]
len_titles = 1
curr_num = 666
while True:
    if len_titles > n:
        break

    curr_num += 1
    if "666" in str(curr_num):
        titles.append(curr_num)
        len_titles += 1

print(titles[n - 1])
