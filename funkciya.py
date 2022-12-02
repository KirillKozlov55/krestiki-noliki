list = ["1 ","2 ","3","4","5","6","7","8","9"]
print(list)


def field():
    for i in range(3):
        print("|",list[0 + i * 3] ,"|",list[1 + i * 3], "|",list[2 + i * 3] , "|")



win = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(3,5,7),(1,5,9)]
def check_win():
    for ind in win:
        if (list[ind[0] - 1] == list[ind[1] - 1] == list[ind[2] - 1]):
            return list[ind[1]-1]
    else:
        return False


def _input(x_o):
    while True:
        value = str(input("куда поставим " + x_o + " ?"))
        if not ( value in "123456789"):
            print("введите число от 1_9")
            continue
        value = int(value)
        if list[value - 1] in "xo":
            print("эта клетка занята")
            continue
        else:
            list[value - 1] = x_o
            break







def konec():
    counter = 0
    while True:
        field()
        if counter % 2 == 0:
            _input("x")
        else:
            _input("o")

        if counter > 3:
            winer = check_win()
            if winer:
                field()
                print(winer, "выиграл")
                break
        counter += 1
        if counter > 8:
            print("ничья")
            break


konec()




#whix pass
