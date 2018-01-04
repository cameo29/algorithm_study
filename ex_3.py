'''
입력은 T 개의 테스트 케이스로 구성된다. 입력의 첫 행에는 T 가 주어진다.
각 테스트 케이스는 공백 하나로 구분되는 두 개씩의 정수로 구성된 세 행으로 이뤄지며, 각각 임의의 세 점의 x와 y 좌표이다. 브라우저 뷰포트의 맨 왼쪽 위 픽셀의 좌표는 (1, 1)이고, 
맨 오른쪽 아래 픽셀의 좌표는 (1000, 1000)이다. 모든 좌표는 뷰포트 안에 위치하며, 각 점의 위치는 모두 다르다.

출력
각 테스트 케이스에 대해 한 행에 하나씩 좌표가 주어지지 않은 나머지 한 점의 x와 y 좌표를 공백 하나로 구분하여 출력한다.
'''
import sys

a = lambda: sys.stdin.readline()
rl = int(a())
n = rl*3
matrix = []
x = []
y = []

for i in range(n):
    b = lambda: sys.stdin.readline()   
    matrix.append(b())

for i in range(rl):
    for j in range(3):
        string = matrix.pop(0)
        string2 = string.split(' ')
        x.append(string2[0])
        y.append(string2[1])
    x4 = int(x.pop(0))^int(x.pop(0))^int(x.pop(0))
    y4 = int(y.pop(0))^int(y.pop(0))^int(y.pop(0))
    print("%d %d" % (x4, y4))



'''
x1 = 1
x2 = 4
x3 = 15

y1 = 0
y2 = 0
y3 = 4

# XOR 연산 이용
# XOR는 두 비트가 다를 경우에만 1
# x1=x3 , x2=x4 이기때문에 x1^x3=0^x2=x2=x4값이 나옴 y4도 마찬가지
x4 = x1^x2^x3
y4 = y1^y2^y3

print("%d %d" % (x4, y4))
'''