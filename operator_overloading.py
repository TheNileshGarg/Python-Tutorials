## Operator Overloading 

# operator overloading means to define operators for specific classes 
# such that we change the normal meaning of that operator

# eg - + for integers means to add two values 
# + for string means to concatenate them 
# + for list means to return an extened list 

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return ComplexNumber(real_part, imag_part)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

class vect:
    def __init__(self, i, j, k):
        self.i = i 
        self.j = j 
        self.k = k 
    def __add__(self, other):
        return vect(self.i + other.i, self.j + other.j, self.k + other.k)
    def __sub__(self, other):
        return vect(self.i - other.i, self.j - other.j, self.k - other.k)
    def __mul__(self, other):
        return (self.i*other.i + self.j*other.j + self.k + other.k)
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

if __name__ == '__main__':
    c1 = ComplexNumber(1, 3)
    c2 = ComplexNumber(7,3)

    c3 = c1 + c2 
    print(f"({c1}) + ({c2}) = {c3}")

    c4 = c1 - c2
    print(f"({c1}) - ({c2}) = {c4}")

    c5 = c1*c2 
    print(f"({c1}) * ({c2}) = {c5}")

    c6 = c1/c2
    print(f"({c1}) / ({c2}) = {c6}")

    v1 = vect(1,2,3)
    v2 = vect(4,5,6)

    v3 = v1 + v2 
    v4 = v1 - v2
    print(f"({v1}) + ({v2}) = {v3}")
    print(f"({v1}) - ({v2}) = {v4}")