class movie:
    def fan(self,speed):
        self.speed=speed
    def light(self):
        print("lights on")
    def display(self):
        self.speed
        print("fan on",self.speed)
sai=movie()
sai.fan(20)
sai.light()
sai.display()
class ecee(movie):
    def light(self):
        print("ok,swiching on the light")
    def fan(self,speed):
        print("fan is on",speed)
        self.v=speed
    def cpu(self):
        print("system is on",self.v)
k=ecee()
k.fan(30)
k.light()
k.cpu()
class shopping(ecee):
    def dress(self,duw):
        self.d=duw
    def price(self,p):   
        self.h=p
    def size(self,s):
        self.v=s
    def display(self):
        print("display dress",self.d,self.h,self.v)
sai=shopping()
sai.dress("shirt")
sai.price("below5000")
sai.size("size32")
sai.display()