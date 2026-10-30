class Rectangle:
    def get_area(self):
        return self.width * self.height

rectangle = Rectangle()

rectangle.width = 8
rectangle.height = 5

rectangle.get_area()

area = rectangle.get_area()

print(area)
