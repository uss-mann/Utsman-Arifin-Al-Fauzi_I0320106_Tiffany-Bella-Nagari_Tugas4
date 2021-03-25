#strings

needle = "HA"
haystack = "Hello World"

#check
if needle in haystack:
    print(needle, "is present in the string", haystack)
else:
    print("Not found")