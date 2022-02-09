import numpy as np
from googlesearch import search

# Google Search
# Mugi F.
# github.com/mugi789
# 2022-02-09

print("""\
        \033[31m
┏━━━┓━━━━━━━━━━━━┏┓━━━━━┏━━━┓━━━━━━━━━━━━━━━━┏┓━━
┃┏━┓┃━━━━━━━━━━━━┃┃━━━━━┃┏━┓┃━━━━━━━━━━━━━━━━┃┃━━
┃┃━┗┛┏━━┓┏━━┓┏━━┓┃┃━┏━━┓┃┗━━┓┏━━┓┏━━┓━┏━┓┏━━┓┃┗━┓
┃┃┏━┓┃┏┓┃┃┏┓┃┃┏┓┃┃┃━┃┏┓┃┗━━┓┃┃┏┓┃┗━┓┃━┃┏┛┃┏━┛┃┏┓┃
┃┗┻━┃┃┗┛┃┃┗┛┃┃┗┛┃┃┗┓┃┃━┫┃┗━┛┃┃┃━┫┃┗┛┗┓┃┃━┃┗━┓┃┃┃┃
┗━━━┛┗━━┛┗━━┛┗━┓┃┗━┛┗━━┛┗━━━┛┗━━┛┗━━━┛┗┛━┗━━┛┗┛┗┛
━━━━━━━━━━━━━┏━┛┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━┗━━┛━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        \033[0m""")
kata = input("  Input Dork : \033[33m")
nomor = input("\033[0m  How much do you want? (Max 100) : \033[33m")
hasil = np.array(search(kata, num_results=int(nomor)-1))
link = format('\n'.join(hasil))
print("\033[0m\033[35m=\033[0m"*15 + " Result " + "\033[35m=\033[0m"*15)
print(link)
print("\033[35m=\033[0m"*38)
print(" Total : " + str(link.count('\n')+1))
print("\033[35m=\033[0m"*38)

def pilihan():
        print(" 1. Save to file")
        print(" 2. Exit")
        choice = input(" >>> ")
        choice = int(choice)
        if choice == 1:
                namafile = input(" Name : ")
                f = open(namafile, "w")
                f.write(link)
                print(" OK! File saved")
                f.close()
        elif choice == 2:
                print(" Bye")
                exit()
        else:
                print(" \033[31m Wrong input number\033[0m")
                pilihan()
pilihan()