if __name__ == '__main__':

    # write
    a =open('aaa.txt', 'w')
    # a.close()

    for b in range(1, 11):
        c =f'{b}  '
        a.write(c)
    a.close()
    # -> wirte - 1  2  3  4  5  6  7  8  9  10

    # read
    d =open('aaa.txt', 'r')
    e =d.read()
    print(e)
    # d.close()
    # -> 1  2  3  4  5  6  7  8  9  10

    # 파일의 모든 라인을 읽어오기
    while True:
        f =d.readline()
        if not f :break
        print(f)
    d.close()

    # 모든 줄을 읽어오고, 각각의 줄을 리스트로 받아옴
    g =open('aaa.txt', 'r')
    h =g.readlines()
    print(h)
    g.close()
    # -> ['1  2  3  4  5  6  7  8  9  10  ']

    # 파일에서 읽어올 때 "\n" 제거
    i =open('aaa.txt', 'r')
    j =i.readlines()
    for k in j:
        k =k.strip()
        print(k)
    i.close()
    # -> 1  2  3  4  5  6  7  8  9  10

    # add
    l =open('aaa.txt', 'a')
    for m in range(11, 21):
        n =f'{m}  '
        l.write(n)
    l.close()

    o =open('aaa.txt', 'r')
    p =o.read()
    print(p)
    o.close()
    # -> 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20

    # with
    with open('aaa.txt', 'a') as q:
        for r in range(21, 31):
            q.write(f'{r}  ')
        print()

    s =open('aaa.txt', 'r')
    t =s.read()
    print(t)