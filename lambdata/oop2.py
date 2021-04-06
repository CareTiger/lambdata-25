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
    def __repr__(self):
        return '({}, {}i)'.format(self.r, self.i)


class SocialMediaUser:
    def __init__(self, name, location, upvotes=0, secondary_upvotes=0):
        self.name = name
        self.location = location
        self.upvotes = upvotes
        self.secondary_upvotes = secondary_upvotes
        self.total_upvotes = self.upvotes + self.secondary_upvotes
    def recieve_upvotes(self, num_upvotes):
        self.upvotes += int(num_upvotes)
        # possible alternative: self.total_upvotes += self.upvotes + self.secondary_upvotes
    def is_popular(self):
        return self.total_upvotes > 100


class Animal:
    """General representation of an animal"""
    def __init__(self, name, weight, diet_type):
        self.name = str(name)
        self.weight = float(weight)
        self.diet_type = str(diet_type)
    def run(self):
        return "Vroom, Vroom, I go quick!"
    def eat(self, food):
        return "Huge fan of that {}".format(food)
    def __repr__(self):
        return f"I am an Animal named {self.name}"


class Sloth(Animal):
    pass


if __name__ == '__main__':
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
    print("Not printed when imported, p   rinted only when file executed")