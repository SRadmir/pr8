def isdigit(di):
        return di.lstrip('-').replace('.', '', 1).isdigit()
while True:
        a = input("Введите число а:")
        if a.lower() == 'stop' or  a.lower() == 'break':
                break
        if not isdigit(a):
                print("Некорректный ввод ")
                continue
        a=float(a)
        b= input("Введите число b:")

        if not isdigit(b):
                print("Некорректный ввод")
                continue
        b=float(b)
        if a<b:
                for i in range(int(a)-1,int(b)+1):
                        if a<i<b:
                                print(i)
                                continue
        elif a>b:
                for i in range(int(b)-1, int(a)+1):
                        if b<i<a:
                                print(i)
                                continue
        else:
                print("a и b равны")
