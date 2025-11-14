class emp:
        def __init__(self,IQ,speed,power):
                self.IQ = IQ
                self.speed = speed
                self.power = power
        def double_speed(self):
                self.speed *= 2

        def double_IQ(self):
                self.IQ *= 2

    
        def double_power(self):
                self.power *= 2 
        


print("Before training")
print("***************")
sparta = emp(20,70,100)
monk = emp(100,50,5)

print(f"Sparta speed: {sparta.speed}\nSparta power:{sparta.power}\nSparta IQ:{sparta.IQ}\n")
print(f"Monk speed: {monk.speed}\nMonk power:{monk.power}\nMonk IQ:{monk.IQ}")

sparta.double_speed()
monk.double_IQ()
monk.double_speed()

print("***************")



print("After training")
print("******************")
print(f"Sparta speed: {sparta.speed}\nSparta power:{sparta.power}\nSparta IQ:{sparta.IQ}\n")
print(f"Monk speed: {monk.speed}\nMonk power:{monk.power}\nMonk IQ:{monk.IQ}")
print("********************")