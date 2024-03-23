class carshowroon:
    import csv
    def registration(self,username,password):
        self.username=username
        self.password=password
        with open("E-com_proj/user_reg.csv","a",newline="") as file:
            store=csv.writer(file)
            store.writerrow(self.username,self.password)
    def login(self,username,password):
        with open("E-com_proj/user_reg.csv","r",newline="") as file:
            read=csv.Dictreader(file)
            for row in read:
                if row[]
