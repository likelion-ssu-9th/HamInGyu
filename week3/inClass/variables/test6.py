a = {'name': "함인규", 'age' : 25, 'singer': ['김','나','박','이']}
print(a)

a["like"] = "lion"
print(a)

del a["age"]
print(a)

print(a.items())
print(a.get('singer'))
print(a['singer'])