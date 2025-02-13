class timeclass:
    def __init__(self, x, y, z):
        self.hours = x
        self.minutes = y
        self.seconds = z
    
    def show(self):
        print(f"The time is {self.hours}h {self.minutes}mins and {self.seconds}s")

    def allhours(self):
        return self.hours + (self.minutes/60 + self.seconds/(60**2))
    
    def allminutes(self):
        return (self.hours * 60) + self.minutes + (self.seconds/60)

    def allseconds(self):
        return (self.hours*60*60) + self.minutes*60 + self.seconds
    

racetime1 = timeclass(1, 30, 5)
racetime1.show()