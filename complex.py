class complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i



    def __add__(self,x):
        return complex(self.r + x.r , self.i + x.i)
    

    def __mul__(self, x):
        r = self.r * x.r - self.i * x.i
        i = self.r * x.i + self.i * x.r
        return complex(r, i)
    

    def __str__(self):
        return f"{self.r} + {self.i}i"
    

c1 = complex(2,5)
c2 = complex(4,7)  



print(f"Their sum is {c1 + c2}")   
print(f"Their product is {c1*c2}")