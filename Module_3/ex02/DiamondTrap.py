from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """The mad King himself"""

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.eyes = "brown"
        self.hairs = "dark"

    def set_eyes(self, color):
        """Setter for eye color."""
        self.eyes = color

    def set_hairs(self, color):
        """Setter for hair color."""
        self.hairs = color

    def get_eyes(self):
        """Getter for eye color."""
        return self.eyes

    def get_hairs(self):
        """Getter for hair color."""
        return self.hairs
