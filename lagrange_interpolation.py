a = int(input("Enter the length of data set: "))
x = []
y = []

for i in range(a):
    b = float(input("Enter value for x: "))
    x += [b]
    c = float(input("Enter value for f(x): "))
    y += [c]

n = a-1

xp = float(input("Enter interpolation value: "))
yp = 0

for i in range(n+1):
    p = 1
    for j in range(n+1):
        if j != i:
            p *= (xp - x[j])/(x[i] - x[j])
    yp += y[i]*p
print("For x= ", xp, ",\ny = ", yp)
