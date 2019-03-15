import time
try:
	print("try")
	time.sleep(10)
	print(1/0)

except Exception as err:
	print("exception")
	print(err)
except:
	print("except")