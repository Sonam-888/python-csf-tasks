temperature = int(input())
user_tem = int(temperature)

if user_tem >= 100:
    print("Boiling")

if 32 < user_tem < 99:
    print("liquid")

if user_tem < 32:
    print("freezing")
