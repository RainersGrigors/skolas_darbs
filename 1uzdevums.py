x = int(input("ievadiet telpas platumu"))
y = int(input("ievadiet telpas garumu"))
def linolejs_izmaksas(linoleja_cena_kvadrātmetrā):
    telpas_izmēri = x*y
    return linoleja_cena_kvadrātmetrā*telpas_izmēri

print(linolejs_izmaksas(3,45))
    
    

