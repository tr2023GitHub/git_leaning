import pytest

from Lesson.calculator import calculator
def test_plus():
   assert  calculator('2+2') == 4
def test_no_signs():
     with pytest.raises(ValueError) as error: # контекстный менеджер with
         calculator('absdfgh')
     assert 'Выражение должно содержать хотя бы один знак (+-/*)' == error.value.args[0]
def test_two_signs():
    with pytest.raises(ValueError) as error:  # контекстный менеджер with
        calculator('2+2+2')
    assert 'Выражение должно содержать 2 целых числа и 1 знак действия' == error.value.args[0]

if __name__=='main':
    pytest.main()