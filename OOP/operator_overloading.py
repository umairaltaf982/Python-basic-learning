class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, others):
        return self.real + others.real, self.imag + others.imag

c1 = Complex(2, 3)
c2 = Complex(4 , 5)

print(c1 + c2)