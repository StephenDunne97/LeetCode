thisdict =	{
    "a":"a",
    "b":"b",
    "c":"c",
    "d":"d",
    "e":"e",
    "f":"f",
    "g":"g",
    "h":"h",
}

substring = ""
x = "i"
if x in thisdict.keys():
    print("Duplicate")
else:
    print("New")
    thisdict[x] = x
    substring = substring + x

print("Substring",substring)
print(thisdict.values())
