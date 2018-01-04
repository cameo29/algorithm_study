# MERCY 2018_01_03
'''
while True:
    a = input("정수입력")
    try:
        b = int(a)
        if b <= 10:
            for i in range(0,b):
                print("Hello Algospot!")

            break
        else:
            print("retry")
        
    except:
        print("type error, retry")
'''
import sys
a = lambda: sys.stdin.readline()
b = int(a())
for i in range(b):
    print("Hello Algospot!")
    