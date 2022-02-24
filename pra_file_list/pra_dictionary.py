if __name__ == '__main__':

    # 코틀린의 Map을 생각
    # 딕셔너리는 "{ }"를 사용
    dic_alphabet ={'aaa' : 111, 'bbb' : 222}
    print(dic_alphabet)
    # -> {'aaa': 111, 'bbb': 222}

    # 키 값이 숫자도 가능
    dic_num ={111 :'aaa', 222 :'bbb'}
    print(dic_num)
    # -> {111: 'aaa', 222: 'bbb'}

    # 딕셔너리에 리스트 값 넣기도 가능
    dic_list ={'aaa' : [1,2,3,4,5]}
    print(dic_list)
    # -> {'aaa': [1, 2, 3, 4, 5]}

    # 딕셔너리에 값 추가
    dic_append ={}
    dic_append['aaa'] =111
    dic_append[222] ='bbb'
    print(dic_append)
    # -> {'aaa': 111, 222: 'bbb'}

    # 딕셔너리 값 삭제
    dic_delete ={'aaa' :111, 'bbb' :222, 'ccc' :333}
    del dic_delete['aaa']
    print(dic_delete)
    # -> {'bbb': 222, 'ccc': 333}

    # 딕셔너리의 키 값 구하기
    print(dic_num.keys(), dic_append.keys())
    # -> dict_keys([111, 222]) dict_keys(['aaa', 222])

    # 딕셔너리의 밸류 값 구하기
    print(dic_num.values(), dic_append.values())
    # -> dict_values(['aaa', 'bbb']) dict_values([111, 'bbb'])

    # 키 값을 받아온 후 리스트로 넘기기
    dic_key_list =list(dic_alphabet.keys())
    print(dic_key_list)
    # -> ['aaa', 'bbb']

    # 특정 값이 딕셔너리에 있나 확인
    print(ccc in dic_alphabet)
    # -> 오류