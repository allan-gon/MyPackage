class Complex:
    def __init__(self, real_part, imaginary_part):
        self.real = real_part
        self.imaginary = imaginary_part

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

    def __repr__(self):
        return f"({self.real}, {self.imaginary})"

    def __add__(self, other_inst):
        real = self.real + other_inst.real
        imaginary = self.imaginary + other_inst.imaginary
        return f"{real} + {imaginary}i"
