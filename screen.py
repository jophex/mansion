li = ["entrance"]

sc = ["food", "others", "descry"]
current = li[len(li) - 1]
size = len(li)
while True:
    print(current)
    choice = input("enter choice")
    if choice == "b" and size == 1:
        print("LAsT ScReEN")
    elif choice == "b" and size > 1:
        print(f"your were in {current}")
        last = li[len(li) - 1]
        li.remove(last)
        current = li[len(li) - 1]
        size = len(li)
    if choice == "a":
        name = input("Enter csn name")
        li.append(name)
        current = li[len(li) - 1]
        size = len(li) - 1
    if choice == "c":
        print(f"you were in {current}")
        print(f"you have {size} screens")
        print(f"you have {sc}")
    if choice == "q":
        break
print("bye")


