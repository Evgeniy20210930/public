import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        """Проверка корректности функции умножения калькулятора"""
        assert self.calc.multiply(self,2,2)==4

    def test_division_calculate_correctly(self):
        """Проверка корректности функции деления калькулятора"""
        assert self.calc.division(self,6,2)==3

    def test_subtraction_calculate_correctly(self):
        """Проверка корректности функции вычитания калькулятора"""
        assert self.calc.subtraction(self,10,5)==5

    def test_adding_calculate_correctly(self):
        """Проверка корректности функции сложения калькулятора"""
        assert self.calc.adding(self,1,3)==4

