masa= int(input("ievadiet masu, kā veselu skaitli"))
def ensteins(masa):
    c=300000000
    gaismas_ātrums=c*c
    return gaismas_ātrums* masa
a= ensteins(masa)
print(a)