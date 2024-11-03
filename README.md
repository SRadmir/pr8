# Это практическая работа №8 
## задание 1 ##
### код
```
while True:
    a = input('введите целое число а или "q" для завершения ' )
    if a == "q":
        break
    a = int(float(a))
    b = int(input('введите целое число b ' ))
    print('сумма = ',a+b);
    continue 

```
## задание 2 ##
```
for i in range(0,10):
        if i == 0 or i ==9 :
                print('*'*10)
        else:
                print('*','  '*8, '*')
```
## задание 3 ##

```
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


```
## задание 4 ##
```
l=0
while True:

        a = input("введите число или ('stop' или 'end' для завершения) ")
        if a=='end' or a == 'stop':
                  print(l)
                  break
        elif a!='stop' or a!= 'end':
                l+=float(a)
                 
```
