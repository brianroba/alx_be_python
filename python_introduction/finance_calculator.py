mon_inc = int(input("Enter your monthly income: "))
mon_exp = int(input("Enter your total monthly expenses: "))
mon_sav = int(mon_inc - mon_exp)
ann_sav = int(mon_sav * 12 + (mon_sav * 12 * 0.05))
#print(f"Your monthly savings are $",mon_sav)

print(f"Your monthly savings are ${mon_sav}.")

print(f"Projected savings after one year, with interest, is: ${ann_sav}")