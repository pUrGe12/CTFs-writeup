from sympy.ntheory import factorint

number = 510143758735509025530880200653196460532653147
factors = factorint(number)

print(f"The factors of {number} are:")
for factor in factors:
    print(f"{factor}^{factors[factor]}")
