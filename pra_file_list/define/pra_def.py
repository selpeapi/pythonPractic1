if __name__ == '__main__':

    # def 함수
    def aaa(a, b):
        c =a+b
        print(c)

    aaa(1,2)
    # -> 3

    def bbb(a, b):
        c =a+b
        print(c)

    # -> 매개변수를 지정하고 값을 넣으면 순서 상관 X
    bbb(b=3, a=4)
    # -> 7

    # -> 불특정 수의 값을 매개변수로 입력 받을 때
    def ccc(*ran):
        rlt =0
        for a in ran:
            rlt =a
            print(rlt, end=' ')

    ccc(1,2,3,4,5)
    # -> 1 2 3 4 5

    # global 변수
    d =0

    def ddd():
        print()
        global d
        d +=1
        return d

    print(ddd())
    # -> 1

    # lambda, 람다
    eee =lambda e,f: e*f
    print(eee(3,5))
    # -> 15
