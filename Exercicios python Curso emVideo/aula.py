c = float(input("Capital inicial:"))
i = float(input("Qual a taxa de juros anual?"))
i = i / 100
t = int(input("Quantos anos?"))
# t = t * 12
m = c * (1+ i) ** t
print(f"Final: {m:.2f}")