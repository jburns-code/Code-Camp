class Rectangle:
    
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self,width):
        """
        Updates the current instances width
        """
        self.width = width
        pass


    def set_height(self,height):
        """
        Updates the current instances height
        """
        self.height = height
        pass


    def get_area(self):
        """
        Calculates the area of a polygon, given the height and width
        """
        return self.width * self.height


    def get_perimeter(self):
        """
        Calculates the perimeter of a polygon, given the height and width
        """
        return 2 * self.width + 2 * self.height


    def get_diagonal(self):
        """
        Calculates the diagoanl length of a polygon, given the height and width
        """
        return (self.width ** 2 + self.height ** 2) ** .5


    def get_picture(self):
        """
        Returns a string in the shape of a polygon made of "*"
        """
        picture = ''
        count = 0
        # determines if width or height are too high a value to be printed
        if self.width > 50:
            return "Too big for picture."
        elif self.height > 50:
            return "Too big for picture."
        
        # add an object (self.width) long, (self.height) amount of times
        while count < self.height:
            picture += '*' * self.width + '\n'
            count += 1    
        return picture


    def get_amount_inside(self,shape):
        """
        Takes a shape, and returns the amount of times the passed in shape
        can fit inside the current shape instance
        """
        fit_height = self.height / shape.height
        fit_width = self.width / shape.width
        return int(fit_height * fit_width)


class Square(Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self,update_side):
        self.width = update_side
        self.height = update_side