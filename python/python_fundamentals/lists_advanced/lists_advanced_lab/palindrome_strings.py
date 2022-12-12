some_strings = input().split()
palindrome_word = str(input())

palindrome_list = []

for pali in some_strings:
    if pali[0] == pali[-1]:
        palindrome_list.append(pali)


print(palindrome_list)
print(f"Found palindrome {palindrome_list.count(palindrome_word)} times")
