X = float(input("Enter X: "))
result = 0
SIZE = int(input("Enter the size of the lists: "))
ListofX = []
ListOfY = []
FirstPoint = []
SecondPoint = []
ThirdPoint = []

for x in range(SIZE):
    ListofX.append(int(input(f'x{x + 1} : ')))
for y in range(SIZE):
    ListOfY.append(int(input(f'y{y + 1} : ')))

for i in range(SIZE - 1):
    if ListofX[i] == X:
        ThirdPoint = [ListofX[i], ListOfY[i]]
        break
    elif ListofX[i] < X < ListofX[i + 1]:
        FirstPoint = [ListofX[i], ListOfY[i]]
        SecondPoint = [ListofX[i + 1], ListOfY[i + 1]]
        break

if ThirdPoint and ThirdPoint[0] == X:
    print(f" value at x = {X} is y = {ThirdPoint[1]}")
else:

    result =  (X - FirstPoint[0]) * (SecondPoint[1] - FirstPoint[1]) / (SecondPoint[0] - FirstPoint[0]) + FirstPoint[1]
    print(f" value at x = {X} is y = {result}")
