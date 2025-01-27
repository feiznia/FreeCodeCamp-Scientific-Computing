import math


class Rectangle():

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

    def set_width(self, w):
        self.width = w
        if type(self) == "Square": self.height = w

    def set_height(self, h):
        self.height = h
        if type(self) == "Square": self.width = h

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2* self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        picture = ""
        if self.width > 50 or self.height > 50: return "Too big for picture."
        for i in range(0, self.height):
            picture = picture + (self.width * "*") + "\n"
        return picture

    def get_amount_inside(self, shape):
        return math.trunc(self.get_area() / shape.get_area())


class Square(Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return "Square(side=" + str(self.width) + ")"

    def set_side(self, side):
        self.width = side
        self.height = side
    
    def set_width(self, width):
        self.width = width
        self.height = width
    
    def set_height(self, height):
        self.width = height
        self.height = height
