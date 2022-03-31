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