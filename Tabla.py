import numpy as np
import sys

bandas = ["L-band", "C-band", "  S-band"]
frecuencia = ["100 GHz", "50 GHz"]
magnitud = ["THz", "nm"]

with open('tabla.txt', 'w') as archivo:
    sys.stdout = archivo

    print("-" * 120)
    print("\t     ", "\t\t\t\t        ".join(map(str, bandas)))
    print("-" * 120)
    print("   ", "\t\t".join(map(str, frecuencia)), end="")
    print("\t\t    ", "\t\t   ".join(map(str, frecuencia)), end="")
    print("\t      ", "\t\t     ".join(map(str, frecuencia)))
    print("-" * 15, end="")
    print("    ", "-" * 15, end="")
    print("     ", "-" * 15, end="")
    print("     ", "-" * 15, end="")
    print("     ", "-" * 15, end="")
    print("     ", "-" * 16)
    print("     ".join(map(str, magnitud)), end="")
    print("\t   ","     ".join(map(str, magnitud)), end="")
    print("\t\t","     ".join(map(str, magnitud)), end="")
    print("\t     ", "     ".join(map(str, magnitud)), end="")
    print("\t  ", "     ".join(map(str, magnitud)), end="")
    print("\t       ", "     ".join(map(str, magnitud)))
    print("-" * 120)

    fs1 = 188.00
    fs5 = 180.05
    fc1 = 193.00
    fc5 = 193.05
    fc1 = 193.00
    fc5 = 193.05
    f1 = 198.00
    f5 = 198.05

    def long_onda(f):
        c = 299792458
        f = f * 1e12
        lamnda = (c / f) * 1e9
        return lamnda

    for _ in range(11):
        fs1l = long_onda(fs1)
        fs5l = long_onda(fs5)
        fc1l = long_onda(fc1)
        fc5l = long_onda(fc5)
        f1l = long_onda(f1)
        f5l = long_onda(f5)
        print(f'{fs1:.2f}  {fs1l:.2f}    ',end=" ")
        print(f'{fs5:.2f}  {fs5l:.2f}     ',end=" ")
        print(f'{fc1:.2f}  {fc1l:.2f}     ',end=" ")
        print(f'{fc5:.2f}  {fc5l:.2f}     ',end=" ")
        print(f'{f1:.2f}  {f1l:.2f}     ',end=" ")
        print(f'{f5:.2f}  {f5l:.2f}    ')
        fs1 += 0.1
        fs5 += 0.1
        fc1 += 0.1
        fc5 += 0.1
        f1 += 0.1
        f5 += 0.1

    print("-" * 120)

sys.stdout = sys.__stdout__