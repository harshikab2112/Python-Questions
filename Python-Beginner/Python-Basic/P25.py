a=input("Enter a string: ")
if a.isdigit() or (a.startswith("-") and a[1:].isdigit()):
    print(True)
else:
    print(False)