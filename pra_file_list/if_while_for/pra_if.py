if __name__ == '__main__':

    a = 1
    b = 2
    c = 3
    d = 4가
    # if, else if, else
    if a >= b:
        print(f'a의 값은 {b} 보다 큽니다')
    elif a <= b:
        print(f'a의 값은 {b}보다 작습니다')
    else:
        print(f'a의 값은 {b}보다 크지도 작지도 않으나 같지도 않습니다')
    # -> a의 값은 2보다 작습니다

    # and, or, not
    if a <= b and b <= c:
        print('a는 b보다 작고 b는 c보다 작습니다')
        # -> a는 b보다 작고 b는 c보다 작습니다
    elif a <= b or b >= c:
        print('a는 b보다 작거나 b는 c보다 큽니다')

    # not은 거짓이 참(결과가 반대)
    if not a >= b:
        print('a는 b보다 과연 클까요?')

    # in, not in
    num_list =[1,2,3,4,5]
    print(1 in num_list)
    # -> True

    str_str ='abcde'
    print('f' not in str_str)
    # -> True

    # pass
    if a >b:
        pass
    # -> pass는 결과가 참일 때 조건 수행 없이 패스
