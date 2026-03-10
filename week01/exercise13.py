email = "  User.Name@Example.COM  "
a = email.strip()
print(a)
b = a.lower()
print(b)
print("@" in email and "." in email)
d = b.split("@")
print(d)
e = a + b
print(e)

csv_line = "Alice,25,Beijing,90.5"
f = csv_line.split(",")
print(f)
g = "|".join(f)
print(g)
h = float(f[3])
print(h)

path = r"C:\Users\admin\Documents\project\main.py"
i = path.split("\\")
j = i[-1]
print(j)
k = j.split(".", 1)
print(k)

word = "racecar"
def is_palindrome(word):
    reverse = word[::-1]
    return word == reverse

print(is_palindrome(word))
print(is_palindrome("hello"))
print(is_palindrome("madam"))