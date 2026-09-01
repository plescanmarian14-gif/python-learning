from collections import Counter
text="The car is black with white"
text=text.split()
count=len(text)
print(f"Avem:{count:>5}")
nr_cuv=0
for i in range(count):
    nr_cuv+=len(text[i])
print(f"Avem:{nr_cuv:>5} litere")
print(f"Primul cuvant {text[0]} , iar ultimul cuvant este {text[-1]}")
text=" ".join(text)
if text==text[::-1]:
    print(f"{text}  este palindroma")
else:
    print("Nu este!")