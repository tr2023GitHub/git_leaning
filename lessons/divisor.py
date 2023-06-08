# import doctest               - необходимо при ручном тесте , до вкл. в Unittest
def divide(a:int,b:int)->int:
    """
Делит первое число на второе и возвращвет на результат плюс 1
    :param a: целое число ( делимое )
    :param b: целое число (делитель)
    :return:  результат деления ( целое число )
    :raise ValueError: если делитель равен нулю
    >>> divide(10,5)
    3
    >>> divide(2,2)
    2
    """
    if b==0:
        raise ValueError('На 0 делить нельзя')
    return a//b + 1
pass
#if __name__=='__main__': - необходимо при ручном тесте , до вкл. в Unittest
#    doctest.testmod()    - необходимо при ручном тесте , до вкл. в Unittest
pass
#