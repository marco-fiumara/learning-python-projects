print("Write how many ml of water the coffee machine has:")
water = int(input())
print("Write how many ml of milk the coffee machine has:")
milk = int(input())
print("Write how many grams of coffee beans the coffee machine has:")
coffee = int(input())
print("Write how many cups of coffee you will need:")
cups = int(input())
total_cups = min([water // 200, milk //
                  50, coffee // 15])

if total_cups > cups:
    print(
        f"Yes, I can make that amount of coffee (and even {total_cups - cups} more than that)")
elif total_cups == cups:
    print("Yes, I can make that amount of coffee")
else:
    print(f"No, I can make only {total_cups} cups of coffee")
