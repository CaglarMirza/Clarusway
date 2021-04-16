right = {'r', 't', 'e', 'c', 'f', 'z', 'q', 'b', 's', 'x', 'w', 'a', 'd', 'g', 'v'}
left = {'n', 'y', 'i', 'l', 'u', 'o', 'j', 'm', 'k', 'h', 'p'}
word = set("clarusway")
comfortable_word = bool(right &  word) and bool(left & word)
print(comfortable_word)