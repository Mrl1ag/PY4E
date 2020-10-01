score = input("Enter Score: ")
try:
    scr = float(score)
except:
    print("Erro, digite um valor número entre 0.0 e 1.0")
    quit()
if scr < 0:
    print("Erro, digite um valor entre 0.0 e 1.0")
elif scr > 1:
    print("Erro, digite um valor entre 0.0 e 1.0")
elif scr >= 0.9:
    print("A")
elif scr >= 0.8:
    print("B")
elif scr >= 0.7:
    print("C")
elif scr >= 0.6:
    print("D")
elif scr < 0.6:
    print("F")
