class calculator:
    """A class to perform basic vector and scalar calculations."""

    def __init__(self, vector):
        """
        Initialize the calculator with a vector.

        Parameters:
            vector (list): A list of numeric values representing the vector.
        """
        self.vector = vector

    def __add__(self, scalar):
        """
        Perform addition of the vector with a scalar.
        """
        self.vector = [x + scalar for x in self.vector]
        print(f"{self.vector}")
        return self.vector

    def __mul__(self, scalar):
        """
        Perform multiplication of the vector with a scalar.
        """
        self.vector = [x * scalar for x in self.vector]
        print(f"{self.vector}")
        return self.vector

    def __sub__(self, scalar):
        """
        Perform subtraction of a scalar from the vector.
        """
        self.vector = [x - scalar for x in self.vector]
        print(f"{self.vector}")
        return self.vector

    def __truediv__(self, scalar):
        """
        Perform division of the vector by a scalar.
        """
        if scalar == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        self.vector = [x / scalar for x in self.vector]
        print(f"{self.vector}")
        return self.vector
