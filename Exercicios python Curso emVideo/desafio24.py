cidade = input("digite o nome de uma cidade:")
# cidade = cidade.strip()
cidade = cidade.lower().split()
cidade = cidade[0].count("santo")
if cidade >= 1:
    print("A cidade digitada começa com a palavra santo ")
else:
    print("A cidade digitada não começa com a palavra santo")