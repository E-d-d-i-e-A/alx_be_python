class Calculator:
    """A calculator class demonstrating class methods and static methods."""
    
    # Class attribute
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        Does not access class or instance data.
        
        Args:
            a (float): First number
            b (float): Second number
        
        Returns:
            float: Sum of a and b
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        Accesses class attribute through cls parameter.
        
        Args:
            cls: Reference to the class itself
            a (float): First number
            b (float): Second number
        
        Returns:
            float: Product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
