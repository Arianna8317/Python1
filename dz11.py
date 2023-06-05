# нарисовать елочку заданной высоты
while True:
    num = int(input('Введите высоту елочки  от 1 до 10: ')) 
    if num > 0 and num < 10:
        break
space = " "
star = "*"
for i in range(num, 0, -1):
    print(f"{space*i}{star*((num-i)*2+1)}")   