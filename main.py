#1-misol
words = ["dasturlash", "kitob", "shunday", "kompyuter", "ilm", "maktab"]

sorted_words = sorted(words, key=len, reverse=True)

first_longest = sorted_words[1]  
second_longest = sorted_words[2] 

print("1-chi eng uzun so'z:", sorted_words[0])
print("2-chi eng uzun so'z:", sorted_words[1])

#2-misol
word = "Python"

for i, char in enumerate(word, start=1):
    print(f"{i} - {char}")
