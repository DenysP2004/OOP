#оголошення змінних текстового, та цифрових типів(цілих та з плаваючою точкою)
mystring = "Hello"
myfloat = 10.00
myint = 20
# тест типів
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

#операції: додавання чисел, приведення типів
addfloat=myint+myfloat
#перевірка чи вийшов дійсний тип
if isinstance(addfloat, float):
    print("float: %d" % addfloat)
#переведення дійсного типу в стрічку і додавання стрічок
addstring=str(addfloat)+" "+mystring
print(addstring)