import random


class Complex_numb:

    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __str__(self):
        sign = "+" if self.imag > 0 else "-"
        return f"{self.real} {sign} {abs(self.imag)}i"

    def __add__(self, other):
        result = Complex_numb()
        result.real = self.real + other.real
        result.imag = self.imag + other.imag
        return result

    def __mul__(self, other):
        result = Complex_numb()
        result.real = self.real * other.real - self.imag * other.imag
        result.imag = self.imag * other.real + self.real * other.imag
        return result


a = Complex_numb(random.randint(-100, 100), random.randint(-100, 100))
b = Complex_numb(random.randint(-100, 100), random.randint(-100, 100))
print(f"A = {a}")
print(f"B = {b}")
print(f"A + B = {a + b}")
print(f"A * B = {a * b}")
