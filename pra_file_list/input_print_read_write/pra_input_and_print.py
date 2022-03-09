if __name__ == '__main__':

    # input
    # 입력받은 값은 str 타입
    a =input('입력을 해주세요\n')
    print(a)
    # -> abcde

    # print
    print('a''b''c')
    # -> abc
    print('d','e','f')
    # -> d e f

    # end 사용 시 출력 후 행동 지정 가능(ex print, input 등등 가능)
    for g in range(11):
        print(g, end=print(' '))
    # ->0 1 2 3 4 5 6 7 8 9 10
