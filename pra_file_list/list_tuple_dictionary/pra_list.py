if __name__ == '__main__':

    alphabet_list =['aaa', 'bbb', 'ccc']
    print(alphabet_list[0:])
    # -> ['aaa', 'bbb', 'ccc']

    # 여러개의 타입을 동시에 넣을 수 있음
    multi_type_list =['ddd', 323]
    print(multi_type_list)
    # -> ['ddd', 323]

    # 리스트를 만들 때 아무것도 안 넣을 수 있음
    null_add_list =[]
    print(null_add_list)
    # -> []

    # 리스트에 값 추가
    null_add_list.append('asd')
    print(null_add_list)
    # -> ['asd']

    # 리스트 중간에 값 추가
    alphabet_list.insert(3, 'eee')
    print(alphabet_list)
    # -> ['aaa', 'bbb', 'ccc', 'eee']

    # 리스트안 값의 개수 불러오기
    print(len(alphabet_list))
    # -> 4

    # 리스트안 값 제거
    del alphabet_list[-1]
    print(alphabet_list)
    # -> ['aaa', 'bbb', 'ccc']