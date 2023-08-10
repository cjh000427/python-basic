
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def calc_sum(end):
    sum = 0
    for n in range(end + 1):
        sum += n
    return sum

def info():
    print('모듈 임포트 연습!')

inch = 2.54
yard = 0.91
lb = 0.45

# test code...

print('모듈의 이름: ',__name__)

if __name__ == '__main__':
    print('1~100까지의 누적합:', calc_sum(100))
    info()
    print(sub(100, 15))
    print('good')


