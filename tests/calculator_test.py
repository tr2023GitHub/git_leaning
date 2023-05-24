from unittest import TestCase, main
from lessons.calculator import calculator


class CalculationTest(TestCase):

    def test_plus(self):
        self.assertEqual(calculator('2+2'), 4)

    def test_minus(self):
        self.assertEqual(calculator('3-1'), 2)

    def test_mult(self):
        self.assertEqual(calculator('4*4'), 16)

    def test_divide(self):
        self.assertEqual(calculator('10/5'), 2)

    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:   # контекстный менеджер with
            calculator('absdfgh')
        self.assertEqual(f'Выражение должно содержать хотя бы один знак (+-/*)', e.exception.args[0])

    def test_two_signs(self):
        with self.assertRaises(ValueError) as e:   # контекстный менеджер with
            calculator('2+2+2')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак действия', e.exception.args[0])

    def test_many_signs(self):
        with self.assertRaises(ValueError) as e:   # контекстный менеджер with
            calculator('2+3*10')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак действия', e.exception.args[0])

    def test_no_ints(self):
        with self.assertRaises(ValueError) as e:   # контекстный менеджер with
            calculator('2.2+3.0')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак действия', e.exception.args[0])

    def test_strings(self):
        with self.assertRaises(ValueError) as e:   # контекстный менеджер with
            calculator('a+a+b')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак действия', e.exception.args[0])


if __name__ == 'main':
    main()
