secret_number = 777

number = int(input("Entre com um numero: "))

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

while number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    number = int(input("entre com outro numero: "))
print("Well done, muggle! You are free now.")
