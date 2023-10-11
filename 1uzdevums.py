x = int(input("ievadiet telpas platumu"))
y = int(input("ievadiet telpas garumu"))
def linolejs_izmaksas(x,y):
    linoleja_cena_kvadrātmetrā =3.45
    telpas_izmēri = x*y
    return linoleja_cena_kvadrātmetrā*telpas_izmēri
a = linolejs_izmaksas(x,y)
print(a)
    
    

