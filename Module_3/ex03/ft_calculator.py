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

        Parameters:
            scalar (float): The scalar to add to the vector elements.

        Returns:
            list: The updated vector with the result of the addition.
        """
        self.vector = [x + scalar for x in self.vector]
        print(self.vector)
        return self.vector

    def __mul__(self, scalar):
        """
        Perform multiplication of the vector with a scalar.

        Parameters:
            scalar (float): The scalar to multiply the vector elements with.

        Returns:
            list: The updated vector with the result of the multiplication.
        """
        self.vector = [x * scalar for x in self.vector]
        print(self.vector)
        return self.vector

    def __sub__(self, scalar):
        """
        Perform subtraction of a scalar from the vector.

        Parameters:
            scalar (float): The scalar to subtract from the vector elements.

        Returns:
            list: The updated vector with the result of the subtraction.
        """
        self.vector = [x - scalar for x in self.vector]
        print(self.vector)
        return self.vector

    def __truediv__(self, scalar):
        """
        Perform division of the vector by a scalar.

        Parameters:
            scalar (float): The scalar to divide the vector elements by.

        Returns:
            list: The updated vector with the result of the division.

        Raises:
            ZeroDivisionError: If scalar is zero.
        """
        if scalar == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        self.vector = [x / scalar for x in self.vector]
        print(self.vector)
        return self.vector
