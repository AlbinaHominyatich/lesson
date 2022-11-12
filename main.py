try:
    print("start code")
    print(10/0)
    print("no error")
except NameError:
    print("we have an NameError")
except ZeroDivisionError:
    print("we have an ZeroDivisionError")

print("code after capsule")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
try:
    print("start code")
    print(10/0)
    print("no error")
except (NameError, ZeroDivisionError) as error:
    print(error)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
try:
    try:
        print("start code")
        print(dima)
        print("no errors")
    except SyntaxError:
        print("wrong syntax")
except NameError as dima:
    print(dima)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
try:
    print("start code")
    #print(dima)
    print("no errors")
except NameError as dima:
    print(dima)

else:
    print("I am ELSE") #якщо немає помилки
finally:
    print("КОНЕЦ")









