class Book:
    """A class to represent a book with magic methods implementation."""
    
    def __init__(self, title, author, year):
        """
        Constructor: Initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """
        Destructor: Called when the object is about to be destroyed.
        Prints a deletion message with the book's title.
        """
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """
        String representation for end users (human-readable).
        Called by print() and str().
        
        Returns:
            str: Formatted string showing book details
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """
        Official representation for developers (recreatable).
        Called by repr() and in interactive console.
        
        Returns:
            str: String that can recreate the Book instance
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
