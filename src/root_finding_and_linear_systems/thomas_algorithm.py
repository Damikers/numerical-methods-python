m = [[0, -10.45, -2.52, 4.15],
          [4.85, -9.82, -2.25, 6.31],
          [4.15, -8.02, -1.26, 5.25],
          [6.49, -8.78, 0, 14.15]]

a_i = [0, 0, 0, 0]
y_i = [0, 0, 0, 0]

for i in range(3):
    if i == 0:
        a_i[i] = m[i][2] / m[i][1]
       
        y_i[i] = - m[i][3] / m[i][1]
        
    else:
        a_i[i] = m[i][2] / (m[i][1] - m[i][0] * a_i[i - 1])
        
        y_i[i] = (m[i][0]*y_i[i - 1] - m[i][3]) / (m[i][1] - m[i][0] * a_i[i - 1])
        

x = [0, 0, 0, 0, 0]

for i in range(3, -1, -1):
    if i == 3:
        x[i] = (m[i][0] * y_i[i - 1] - m[i][3]) / (m[i][1] - m[i][0] * a_i[i - 1])
    else:
        x[i] = a_i[i] * x[i + 1] + y_i[i]

    
print(f"i |   a_i     |   y_i ")
print("--|-----------|----------")
for i in range(3):
    print(f"{i + 1} | {round(a_i[i], 4):^9} | {round(y_i[i], 4):^9}")

print("\n")

print(f"i  |   x_i   ")
print("---|----------")
for i in range(4):
    print(f"{i + 1}  |  {round(x[i], 4)}   ")