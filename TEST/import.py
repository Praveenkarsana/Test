word=input("Enter a word")
vowel='aeiouAEIOU'
flag=0
for i in vowel:
    if i in word:
        flag=1
    break
    if flag==1:
        print("Word contain vowel")
    else:
        print("Word not contain vowel")        