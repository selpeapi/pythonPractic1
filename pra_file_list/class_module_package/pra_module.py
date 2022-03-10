import pra_class
from pra_class import classvar
from pra_class import calculator, calculator2
from pra_class import *
a =111
# 모듈을 import 해서 불러올 때, '__name__' 아래에 구현된 코드는 false 값을 받아 불러오지 않음
# '__name__' 에 구현된 해당 코드는 본인 파일에서만 ture 값으로 실행 됨
# 해당 파일에서는 'main' 값이, 다른 파일에서는 '이름.py' 에 해당하는 이름이 불러와짐
if __name__ == '__main__':
    print(a)
    # -> 111
    b =pra_class.calculator(1,2)
    print(b.plus())
    # -> 3
    print(pra_class.__name__)
    # -> pra_class
    print(__name__)
    # -> __main__

    print(classvar.aaa)
    # -> 0