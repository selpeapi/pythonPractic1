if __name__ == '__main__':

    a =True
    b =0
    c =1

    # while문
    while a ==True:
        b +=1
        print(b)
        # -> 1~100까지 출력
        if b >= 100: break

    while c <30:
        c +=1
        if c %2 ==0:
            continue
        print(f'c는 홀수고 값은 {c}입니다')
        # -> 3,5,7,9 --> 27,29까지 출력
