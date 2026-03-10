dictionary = {
    "title": "be a python master",
    "auther": "Javatoky",
    "year": 2026,
    "pages": 256,
    "tags": ["python", "coding", "programming", "master", "AI using"]
}

for key, values in dictionary.items():
    print(f"{key}: {values}")

if(dictionary.get("isbn") is None):
    print(f"ISBN未录入")
##print(dictionary.get("isbn", "ISBN未录入"))

dictionary["publisher"] = "xxx出版社"
dictionary["year"] = 2027

del dictionary["pages"]
##pages = dictionary.pop("pages")

for key, values in dictionary.items():
    print(f"{key}: {values}")