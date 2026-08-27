nota=float(input("Give me a note: "))

if nota<5:
    print("Insuficient")
elif nota>5 and nota<6.9:
    print("suficient")
elif nota>7 and nota<8.9:
    print("Bine")
else:
    print("Foarte bine")