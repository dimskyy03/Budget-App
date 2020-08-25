# This entrypoint file to be used in development. Start by reading README.md
import budget
from budget import *


food = budget.Category("Makanan")
food.deposit(1000, "duit awal")
food.withdraw(10.15, "ayam geprek")
food.withdraw(15.89, "chatime")
clothing = budget.Category("Baju")
food.transfer(400, clothing)
print(food)
clothing.withdraw(25.55)
clothing.withdraw(100)
print(clothing)
auto = budget.Category("Dadakan")
auto.deposit(500, "duit simpanan")
auto.withdraw(15)
print(auto)

print(create_spend_chart([food, clothing, auto]))
