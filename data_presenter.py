cupcake_file = open("./CupcakeInvoices.csv")

for row in cupcake_file:
    print(row)

for row in cupcake_file:
    values = row.split(',')
    print(values[2])

for row in cupcake_file:
    values = row.split(',')
    total = int(values[3]) * float(values[4])
    print(total)

total = 0
for row in cupcake_file:
    values = row.split(',')
    total = total + (int(values[3])) * float(values[4])

print(total)

cupcake_file.close()

import matplotlib.pyplot as plt

x = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
y = [10,40,32,84,60,52,18]

plt.plot(x,y)

plt.xlabel('Day Purchased')

plt.ylabel('Cupcakes Purchased')

plt.title('My Cupcake Sales')

plt.show()