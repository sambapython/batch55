'''
to ecplain exceptions and loggin concept
'''
import logging
print("welcome")
logging.basicConfig(level=logging.WARN,
                    filename="log.txt",
                    format="%(asctime)s-->%(levelname)s==>%(message)s")
logging.info("program started")
A = input("enter a value:")
logging.info("a value entered")
B = input("enter b value:")
logging.info("b value entered")
logging.debug("before conversiona=%s,b=%s" % (A, B))
try:
    A = float(A)
    B = float(B)
    logging.debug("after conversiona=%s,b=%s" % (A, B))
    res = A / B
    print(f"Result:{res}")
    logging.debug("Result:%s" % res)
except ZeroDivisionError as err:
    logging.error(err)
    print("don't enter zero for b. b>0")
except ValueError as err:
    logging.error(err)
    print("expecting only digits")
except Exception as err:
    logging.error(err)
    print("something went wrong contact admin.")
print("thank you")
logging.info("end")
