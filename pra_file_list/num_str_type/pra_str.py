if __name__ == '__main__':

    a ='i am hello, world'

    # -> <class 'str'>
    # ' ' 공백을 기준으로 문자열 분리
    # 값은 리스트로 저장
    print(a.split(' '))
    # -> ['i', 'am', 'hello,', 'world']

    # 단일 값을 뽑기 위해서 [] 사용
    print(a.split(' ')[0])
    # -> i
    print(a.split(' ')[1 :-1])
    # -> ['am', 'hello,']
    print(a)
