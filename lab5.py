class classDetail:
    def __init__(self,cN,rN,time,typ):
        self. callerNo, self.receiverNo = cN,rN
        self.time, self.type = time,typ
    
    def getDetails(self):
        print("caller:", self.callerNo, "Reveiver:", self.receiverNo)
        print("Time of call:",self.time,"Type:", self.type)        


class Util:
    def __init__(self):
        self.list_of_call_objects = []
    def parse_customer(self, list_of_call_string):
        for call in list_of_call_string:            
            list_call= call.split(',')            
            temp=classDetail(list_call[0],list_call[1],list_call[2],list_call[3])
            self.list_of_call_objects.append(temp)
            temp.getDetails()



call1='9990300001,980711211,23,STD'
call2='9990900701,980716211,45,STD'
call3='9990915001,980891211,64,ISD'

list_of_call_string =[call1,call2,call3]
Util().parse_customer(list_of_call_string)
