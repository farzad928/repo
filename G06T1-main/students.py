stuInfo = []

class Students:
    def __init__(self, stuName, stuFamily, stuId):
        self.stuName = stuName
        self.stuFamily = stuFamily
        self.stuId = stuId
        dic = dict(name=self.stuName, family=self.stuFamily, id=self.stuId)
        self.dic = dic
        self.stuInfo = stuInfo

    def add(self):
        info = []
        if len(info) == 0:
            info.append(self.dic) 
        else:
            for stu in info:
                if self.dic == stu:
                    print('already')
                    return
                else:
                    info.append(self.dic)                       
            print('alreadu exist')
            return

        for num in info:
            self.stuInfo.append(num)


    def list(self):
        print(self.stuInfo)


farzad = Students('farzad', 'adelfar', 99)
farzad.add()
print(farzad.stuInfo)

ali = Students('ali', 'mamad', 90)
ali.add()
print(ali.stuInfo)

reza = Students('ali', 'adelfar', 98)
reza.add()
print(reza.stuInfo)
