class ecee:
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
    def __init__(self,place):
        print("welcome to shopping",place)
        self.place=place
    def dress(self,duw):
        self.d=duw
    def price(self,p):   
        self.h=p
    def size(self,s):
        self.v=s
    def display(self):
        print("display dress",self.d,self.h,self.v,self.place)
sai=shopping("zudio")
sai.dress("shirt")
sai.price("below5000")
sai.size("size32")
sai.display()
sai.fan(5)
sai.light()
sai.cpu()