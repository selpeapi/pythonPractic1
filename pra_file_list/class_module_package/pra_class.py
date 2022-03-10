import pra_module

print(pra_module.a)


class calculator:
    # __init__은 생성자
    def __init__(self, num0, num1):
        self.num0 = num0
        self.num1 = num1

    def inputnum(self, num0, num1):
        self.num0 = num0
        self.num1 = num1

    def plus(self):
        result = self.num0 + self.num1
        return result

    def minus(self):
        result = self.num0 - self.num1
        return result

    def multiply(self):
        result = self.num0 * self.num1
        return result

    def divide(self):
        result = self.num0 / self.num1
        return result


# 상속
class lowCalculator(calculator):
    # 메소드 오버라이딩
    def divide(self):
        if self.num1 == 0:
            return 0
        else:
            result = self.num0 / self.num1
            return result


# 클래스 변수
class classvar():
    aaa = 0


class calculator2:
    # __init__은 생성자
    def __init__(self, num0, num1):
        self.num0 = num0
        self.num1 = num1

    def inputnum(self, num0, num1):
        self.num0 = num0
        self.num1 = num1

    def plus(self):
        result = self.num0 + self.num1
        return result


if __name__ == '__main__':
    cal1 = calculator(2, 3)

    print(cal1.num0, cal1.num1)
    print(cal1.plus())
    print(cal1.minus())
    print(cal1.multiply())
    # print(cal1.divide())

    a = classvar()
    print(a.aaa)
    # -> 0
    a.aaa = 1
    print(a.aaa)
    # -> 1
    classvar.aaa = 2
    b = classvar()
    print(b.aaa)
    # -> 2
    print(a.aaa)
    # -> 1
