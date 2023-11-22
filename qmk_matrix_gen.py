# script to make qmk matrix for info.json

y = str(input("Number of rows: "))
x = str(input("Number of cols: "))
count = 0
matrix = open("info_gen.json", "w")

for row in range(0, int(y)):
    for col in range(0, int(x)):
        count += 1
        if count >= int(x)*int(y):  # no comma at end
            matrix.write(f'''{{"matrix": [{row}, {col}], "x": {row}, "y": {col}}}\n''')
        else:  # comma at end
            matrix.write(f'''{{"matrix": [{row}, {col}], "x": {row}, "y": {col}}},\n''')
matrix.close()

