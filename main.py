
kwota_kredytu = int(input("Podaj całkowitą kwotę kredytu: "))
kwota_raty = int(input("Podaj kwotę raty: "))
kwota_oprocentowania = int(input("Podaj kwotę oprocentowania kredytu:"))
kwota_pierwsza = kwota_kredytu

inflacja = [1.59282448436825, -0.453509101198007, 2.324671717, 1.261254407, 1.782526286, 2.329384541,
            1.502229842, 1.782526286, 2.328848994, 0.616921348, 2.352295886, 0.337779545, 1.577035247,
            -0.292781443, 2.48619659, 0.267110318, 1.417952672, 1.054243267, 1.480520104, 1.577035247,
            -0.07742069, 1.165733399, -0.404186718, 1.499708521]
nazwa = ["1: ", "2: ", "3: ","4: ","5: ","6: ","7: ","8: ","9: ","10: ","11: ","12: ","13: ","14:",
         "15: ", "16: ", "17: ","18: ","19: ","20: ","21:","22:","23: ","24: "]
i = 0
while i < len(inflacja):
    wzor1 = (1 + ((inflacja[i] + kwota_oprocentowania) / 1200)) * kwota_kredytu - kwota_raty
    kwota_kredytu = wzor1
    pozostało =  kwota_pierwsza - kwota_kredytu
    kwota_pierwsza = kwota_pierwsza - pozostało
    print(f"W {nazwa[i]} Twoja pozostała kwota kredytu to: {round(kwota_kredytu, 2)}. To o {round(pozostało, 1)} mniej niż w zeszłym miesiącu ")
    i = i + 1

