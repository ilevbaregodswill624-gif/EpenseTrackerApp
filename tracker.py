names = []
amounts = []

def show_expenses():
    total = 0 
    for i in range(len(names)):
        print(names[i], "-", amounts[i])
        total += amounts[i]
    print("Total:", total)

def save_expenses():
    file = open("expenses.txt", "w")
    for i in range(len(names)):
        file.write(names[i] + " - " + str(amounts[i]) + "\n")
    file.close()
    print("Saved!")

try:
    file = open("expenses.txt", "r")
    for line in file:
        parts = line.strip().split(" -")
        names.append(parts[0])
        amounts.append(float(parts[1]))
except:
    print("No saved expenses yet.")

while True:
    name = input("What did you spend money on? (Type 'q' to quit): ")
    if name == 'q':
        break
    amount = float(input("How much did you spend? "))
    names.append(name)
    amounts.append(amount)
total = 0
for i in range(len(amounts)):
    print(names[i], "-", amounts[i])
    total += amounts[i]
print("Total: ", total)

file = open("expenses.txt", "w")
for i in range(len(amounts)):
    file.write(names[i] + " - " + str(amounts[i]) + "\n")
file.close()
print("Saved!")
