
# 모듈 내에 존재하는 변수, 함수, 클래스 등을 직접 임포트 하는 방법.
from math import factorial, gcd

print(factorial(6))
print(factorial(10))

print(gcd(12, 18))

# 임포트할 모듈에 별칭을 지정하여 사용하기
import statistics

li = [34, 55, 12, 33, 55, 66, 99]
print('평균:', statistics.mean(li))
print('분산:', statistics.variance(li))
print('표준편차:', statistics.stdev(li))

# 위에서 알려드린 두 가지 개념을 합쳐서도 사용이 가능합니다.
from math import factorial as fac

print(fac(8))

