names=["Alice","Bob","keerthana","Naveen","charlie"]
target="Naveen"
for i in names:
    if i==target:
        print("it is found {}".format(target))
        break
else:
    print("Name not found")

#finding book in shelf
shelf=["getit what you desire", "python","Commercials","central"]
for book in shelf:
    if book=="python":
        print("found")
        break
else:
    print("book not found")