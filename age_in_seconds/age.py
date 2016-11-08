class Age():

    def __init__(self,age):
        self.age     = age
        self.days    = 365
        self.hours   = 24
        self.minutes = 60
        self.seconds = 60

    def age_to_seconds(self):
        seconds = int(self.age) * self.days * self.hours * self.minutes * self.seconds
        return seconds 