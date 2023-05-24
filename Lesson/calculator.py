def calculator(expression):
    allowed='+-/*'
    if not any(sing in expression for sing in allowed):
        raise ValueError(f'Выражение должно содержать хотя бы один знак ({allowed})')
    for sing in allowed:
        if sing in expression:
            try:
                left,right=expression.split(sing)
                left,right=int(left),int(right)
                return {
                    '+':lambda a,b : a + b,
                    '-':lambda a,b : a - b,
                    '*':lambda a,b : a * b,
                    '/':lambda a,b : a / b
                }[sing](left,right)

#               if sing=="+":
#                  return left+right
#                elif sing=='-':
#                   return  left-right
#                elif sing=='*':
#                   return left*right
#                elif sing=='/':
#                    return left/right
#
            except (ValueError,TypeError):
               raise ValueError ('Выражение должно содержать 2 целых числа и 1 знак действия')

if __name__=='__main__':
     print(calculator('10/5'))
     pass