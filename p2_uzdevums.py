x = int(input("Ievadiet kādu dēļa tipu jūs vēlaties, 1 vai 2"))
a = float(input("Ievadiet cik metrus plats ir jūsu dēlis, skaitli ievadiet decimāldaļās"))
b = float(input("Ievadiet cik metrus biezs ir jūsu dēlis, skaitli ievadiet decimāldaļās"))
c = float(input("Ievadiet cik metrus garš ir jūsu dēlis, skaitli ievadiet decimāldaļās"))
def dēļi(x,a,b,c):
    if x==1:
        y = 145
    elif x==2:
        y= 125
    else:
        print("mums nav tādu dēļu")
    return a*b*c*y
dēļa_cena= dēļi(x,a,b,c)
print(dēļa_cena)