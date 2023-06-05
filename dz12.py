print("                ТАБЛИЦА УМНОЖЕНИЯ")
print()
space = " "
for i in range(2, 7, 4):
    for j in range(2, 11):
        for k in range(0, 4):
            print(f"{ i + k } x ", end = "")
            if j < 10: 
                print (" ", end = "" )
            print(f"{j} = ", end = "" )   
            if j * ( i + k ) < 10 :
               print (" ", end = "")
            print (( i + k )*j,"   ", end = "")
        print()


    print()

