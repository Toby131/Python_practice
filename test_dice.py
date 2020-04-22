'''
목표 : random 외부파일과 그 안에 있는 함수들을 사용해 난수 생성하고 if문에서 난수 사용해 주사위 던지기 예제 구현

결과 : 두사람이 차례대로 주사위 던짐 -> 홍길동 먼저 던져 : 3 -> 김길동 나중에 던져 : 5 -> 승자는 김길동
'''
import random
a=random.random()
print("새로 만든 실수형 난수",a)


'''
random.py 외부 파일에 있는 randint() 함수 기능은 개발자가 지정한 2개의 값 사이에 있는 무작위 정수
'''
import random
b=random.randint(1,6)
print("주사위 난수",b)


'''
random.py 외부파일에 있는 randrange()함수 기능은 개발자가 지정한 3개의 값 사이에 있는 무작위 정수
변수명=random.randrange(시작정수,끝정수,증가폭)
'''
c=random.randrange(1,7,1)
print("1~6사이 임의 정수",c)


'''
1~6사이 정수 중 홀수 중 하나 출력
'''
d=random.randrange(1,7,2)
print("1~6사이 홀수",d)



import random
print("홍길동이 먼저 주사위 던짐")
print("주사위가 땅에 떨어짐")
dice1=random.randint(1,6)
print("홍길동이 던진 주사위 숫자",dice1)

print("김길동이 주사위 던짐")
print("주사위가 땅에 떨어짐")
dice2=random.randint(1,6)
print("김길동이 던진 주사위 숫자",dice2)

if (dice1>dice2):
    print("승자는 홍길동")
else:
    if(dice1==dice2):
        print("무승부")
    else:
        print("승자는 김길동")
    















