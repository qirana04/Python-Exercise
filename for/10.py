#menghitung jumlah huruf vokal dalam string
word = "hello everyone, let me introduce my self"
vowels = "aeiou"
count = 0
for letter in word:
    if letter in vowels:
        count += 1
print("Jumlah huruf vokal:", count)
