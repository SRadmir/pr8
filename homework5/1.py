l=0
while True:

        a = input("введите число или ('stop' или 'end' для завершения) ")
        if a=='end' or a == 'stop':
                  print(l)
                  break
        elif a!='stop' or a!= 'end':
                l+=float(a)
                
