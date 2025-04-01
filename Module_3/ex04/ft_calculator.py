class calculator:
    """A class to perform basic vector and scalar calculations."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> float:
        """
        Calculate the dot product of two vectors.
        """
        result = sum(float(x) * float(y) for x, y in zip(V1, V2))
        print(f"Dot product is: {result}")
        return result

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> list:
        """
        Add two vectors element-wise.
        """
        result = [float(x) + float(y) for x, y in zip(V1, V2)]
        print(f"Add Vector is: {result}")
        return result

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> list:
        """
        Subtract the second vector from the first vector element-wise.
        """
        result = [float(x) - float(y) for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {result}")
        return result
