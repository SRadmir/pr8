a = float(input("Введите число а:"))
b = float(input("Введите число b:"))
l=[]
if a<b:
        for i in range(int(a)-1,int(b)+1):
                if a<i<b:
                        print(i)
elif a>b:
        for i in range(int(b)-1, int(a)+1):
                if b<i<a:
                        print(i)
else:
        print("a и b равны")
