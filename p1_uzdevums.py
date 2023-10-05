x = str(input("Ievadiet vārdu uzvārdu"))
y =int(input("Ievadiet cik stundas jūs esat nostrādājis"))
z =float(input("Ievadiet savu stundas likmi, kā decimāl daļu"))
def alga(y,z):
    if(y > 40):
        stundas_likme = z / 100 * 10 + z
    else:
        stundas_likme=z
    return stundas_likme*y
A = alga(y,z)
print(x,"jūs alga ir ",A,"Eiro")
