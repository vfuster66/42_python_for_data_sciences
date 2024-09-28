from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Baratheon character."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Mark the character as dead."""
        self.is_alive = False

    def __str__(self):
        """String representation of the Baratheon."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Formal representation of the Baratheon."""
        return self.__str__()


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Lannister character."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Mark the character as dead."""
        self.is_alive = False

    def __str__(self):
        """String representation of the Lannister."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Formal representation of the Lannister."""
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool):
        """Class method to create a Lannister character."""
        instance = cls(first_name)
        instance.is_alive = is_alive
        return instance
