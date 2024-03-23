class ecee:
    def light(self):
        print("ok,swiching on the light")
    def fan(self,speed):
        print("fan is on",speed)
        self.v=speed
    def cpu(self):
        print("system is on",self.v)
sai=ecee()
sai.fan(30)
sai.light()
sai.cpu()