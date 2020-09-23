# This is created by sugan😎😍😀
"""First enter your equations and
    press run🏃‍️🏃‍️🏃‍️"""
print("this program is created by sugan under MIT lisence 2.0")


def find(a):
    num1 = a[0]
    num2 = a[1]
    num3 = a[2]
    num4 = a[3]
    num5 = a[4]
    num6 = a[5]

    if num1 == num4:
        if num2 == num5:
            if num3 == num6:
                print("Invalid1")
            else:
                print("Invalid2")
        elif num2 != num5:
            if num3 != num6:
                print('y = ', (num3 - num6) / (num2 - num5), 'x = ',
                      (num3 - (num2 * ((num3 - num6) / (num2 - num5)))) / num1)
                return " "
            elif num3 == num6:
                print('y = 0 and x = ', b[2])
                return " "
            else:
                prit("Invalid3")
        else:
            print("Invalid4")
    elif num1 != num4:
        if num2 == num5:
            if num3 == num6:
                print("x = 0 and y  = ", b[2])
                return " "
            elif num3 != num6:
                print("x =", (num6 - num3) / (num4 - num1), 'y = ', (num3 - num1) / (num2))
                return " "
            else:
                print("Invalid5")
        elif num2 != num5:
            mullist1 = [i * num4 for i in a[:3]]
            mullist2 = [i * num1 for i in a[3:]]
            if mullist1[1] > mullist2[1] or mullist1[1] == mullist2[1]:
                w = mullist1[1] - mullist2[1]
                a = mullist1[2] - mullist2[2]
                s = a / w
                d = (num3 - num2 * s) / num1
                print("x = ", d, "y = ", s)
                return " "
            else:
                w = mullist1[1] - mullist2[1]
                a = mullist1[2] - mullist2[2]
                s = a / w
                d = (num3 - num2 * s) / num1
                print("x = ", d, "y = ", s)
                return " "
        else:
            print("invalid6")
    else:
        print("invalid7")


while True:
    first_equ = str(input().replace(' ', ''))
    second_equ = str(input().replace(' ', ''))
    try:
        listconv1 = first_equ.split('=')
        listconv2 = second_equ.split("=")
        w = listconv1[0].split("x")
        c = w[1].split('y')
        c.remove('')
        w += c
        s = listconv2[0].split("x")
        c = s[1].split('y')
        c.remove('')
        s += c
        d = [[w[0], w[2], listconv1[1]], [s[0], s[2], listconv2[1]]]
        a = []
        for x in d:
            for i in range(len(x)):
                if x[i] == '' or x[i] == '+':
                    x[i] = 1
                elif x[i] == '-':
                    x[i] = -1
                else:
                    x[i] = int(x[i])
            a += x

        print(a)
        print(find(a))
    except:
        print('error')
        break
