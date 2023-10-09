sen = input("Введите текст: ").split()
count = 0
art = ["a", "an", "the"]
s = list()
for i in sen:
    s.append(i.lower())
for i in s:
    for m in art:
        if i == m:
            count += 1
 
print("Общее количество артиклей:", count)