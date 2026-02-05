possible = []

word = input()

wordlen = len(word)

for i in range(wordlen):
  for j in range(i,wordlen):
    palindrome = word[i:j+1]
    if palindrome == palindrome[::-1]:
     possible.append(len(palindrome))

print(max(possible))
