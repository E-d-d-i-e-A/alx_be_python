import math

class Shape:
    """Base class representing a generic shape."""
    
    def area(self):
        """
        Calculate the area of the shape.
        This method must be overridden in derived classes.
        
        Raises:
            NotImplementedError: This method should be implemented by subclasses
        """
        raise NotImplementedError("Subclasses must override the area() method")


class Rectangle(Shape):
    """Derived class representing a rectangle."""
    
    def __init__(self, length, width):
        """
        Initialize a Rectangle instance.
        
        Args:
            length (float): The length of the rectangle
            width (float): The width of the rectangle
        """
        self.length = length
        self.width = width
    
    def area(self):
        """
        Calculate and return the area of the rectangle.
        
        Returns:
            float: The area (length × width)
        """
        return self.length * self.width


class Circle(Shape):
    """Derived class representing a circle."""
    
    def __init__(self, radius):
        """
        Initialize a Circle instance.
        
        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius
    
    def area(self):
        """
        Calculate and return the area of the circle.
        
        Returns:
            float: The area (π × radius²)
        """
        return math.pi * (self.radius ** 2)
