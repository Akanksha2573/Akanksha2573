month=int(input().strip())
if 3<=month<=5:
    print("Spring")
elif 6<=month<=8:
    print("Summer")
elif 9<=month<=11:
    print("Autum")
elif month==12 or 1<=month<=2:
    print("Winter")
else:
    print("Invalid")
