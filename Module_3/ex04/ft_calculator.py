class calculator:
    """A class to perform basic vector and scalar calculations."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> float:
        """
        Calculate the dot product of two vectors.

        Parameters:
            V1 (list): The first vector.
            V2 (list): The second vector.

        Returns:
            float: The result of the dot product.
        """
        result = sum(float(x) * float(y) for x, y in zip(V1, V2))
        print(f"Dot product is: {result}")
        return result

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> list:
        """
        Add two vectors element-wise.

        Parameters:
            V1 (list): The first vector.
            V2 (list): The second vector.

        Returns:
            list: The result of adding the two vectors.
        """
        result = [float(x) + float(y) for x, y in zip(V1, V2)]
        print(f"Add Vector is: {result}")
        return result

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> list:
        """
        Subtract the second vector from the first vector element-wise.

        Parameters:
            V1 (list): The first vector.
            V2 (list): The second vector.

        Returns:
            list: The result of subtracting V2 from V1.
        """
        result = [float(x) - float(y) for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {result}")
        return result
