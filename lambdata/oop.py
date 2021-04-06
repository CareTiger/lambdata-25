"""Module 2 OOP Example Module"""
class BareMinimumClass:
    pass
class Complex():
    """
    This a Complex class that has a real and imaginary attribute
    """
    def __init__(self, real_part, imag_part):
        """
        Constructor for Complex Numbers.
        """
        self.r = real_part  # Complex_Object.r == real_part
        self.i = imag_part  # Complex_Object.i == imag_part
    def add(self, other_complex):
        """
        Adds to complex objects together!
        """
        self.r += other_complex.r
        self.i += other_complex.i
# Complex_num_1_object.r = 3
# Complex_num_1_object.i = -5
Complex_num_1_object = Complex(
    real_part=3,
    imag_part=-5
)
# Complex_num_2_object.r = 2
# Complex_num_2_object.i = 6
Complex_num_2_object = Complex(
    real_part=2,
    imag_part=6
)
Complex_num_1_object.add(Complex_num_2_object)
print(Complex_num_1_object.r, Complex_num_1_object.i)