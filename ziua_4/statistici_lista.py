def media(*numere):
    media=0
    for i in range(len(numere)):
        media+=numere[i]
    media=media/len(numere)
    return media

def max_1(*numere):
    return max(numere)
def min_1(*numere):
    return min(numere)

print(f"media este: {media(10,12,4,5,6)}")
print(f"maximul este: {max_1(10,12,4,5,6)}")
print(f"minimul este: {min_1(10,12,4,5,6)}")