class shopping:
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