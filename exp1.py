import time
print("welcome")
a=input("enter a value:")
b=input("enter b value:")
f=open("data1.txt","w")
print(f"before conversiona={a},b={b}")
f.write(f"before conversiona={a},b={b}")

try:
    a=float(a)
    b=float(b)
    print(f"after conversiona={a},b={b}")
    f.write(f"\nafter conversiona={a},b={b}")
    res=a/b
    print("calculating the result....")
    time.sleep(10)
    print(f"Result:{res}")
    f.write(f"\nResult:{res}")
except ZeroDivisionError as err:
    print(err)
    print("don't enter zero for b. b>0")
except ValueError as err:
    print(err)
    print("expecting only digits")
except Exception as err:
    print(err)
    print("something went wrong contact admin.")
finally:
    print("finally executing")
f.close()
print("thank you")
print("end")