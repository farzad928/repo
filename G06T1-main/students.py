class Students:
    def __init__(self, stuName, stuFamily, stuId):
        self.stuName = stuName
        self.stuFamily = stuFamily
        self.stuId = stuId
        dic = dict(name=self.stuName, family=self.stuFamily, id=self.stuId)
        self.dic = dic
        stuInfo = []
        self.stuInfo = stuInfo

    def add(self):
        pass

    def list(self):
        print(self.stuInfo)

# farzad = Students('farzad', 'adelfar', 99)
# farzad.add()

# ali = Students('ali', 'adelfar', 99)
# ali.add()