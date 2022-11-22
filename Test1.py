ls = []
### READS THE INFO FROM CSV FILE AND CONVERT INTO LIST OF LISTS
with open("readme.csv","r") as f:
    """
    ls = f.read().replace("\n",",").split(".")
    for item in ls:
        print(item)
    print(ls)
    """
    # print(f.read())
    ls = f.read().split("\n")
    for i in range(len(ls)):
        #print("*******")
        ls[i]=ls[i].split(",")
        #print(ls[i])
    f.close()

### ADD "All" INTO EACH STRING TO BE ABLE TO FIND IT WHEN THERES NO FILTER
for i in range(1,len(ls)):
    for j in range(1,len(ls[i])):
        ls[i][j] += "/All"
    
### USER INPUTS
i1 = input("enter min pax")
i2 = input("enter max pax")
i3 = input("enter occasion")
i4 = input("enter location")
i5 = input("enter min time")
i6 = input("enter max time")
i7 = input("enter price")

"""
i1 = "2"
i2 = "3"
i3 = "Friend"
i4 = "Home"
i5 = "1"
i6 = "2"
i7 = "$"
"""

ls_ans = [i1,i2,i3,i4,i5,i6,i7]

### MAKE EMPTY INPUTS INTO "All"
for i in range(len(ls_ans)):
    if ls_ans[i] == "":
        ls_ans[i] = "All"

ls_display = []

### CHECK EVERY LINE AND FILTER
for i in range(1,71):
    appendd = True
    for j in range(1,8):
        print(i,j)
        if ls_ans[j-1] in ls[i][j]:
            pass
        else:
            appendd = False
            break
    if appendd:
        ls_display.append(ls[i][0])

print(ls_display)







