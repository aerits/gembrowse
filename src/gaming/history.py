#!/usr/bin/env python3
import os


class history():
     def __init__(self, p: str, tabId: str):
          self.asdf = p
          self.id = tabId
          self.historyFile = "./history/"+str(self.id)+"history.txt"
          self.timesWentBackInTime = 1

     def writeHistory(self):       
          if(self.timesWentBackInTime > 0):
               print("this is running")
               try:
                    os.remove(self.historyFile)
               except:
                    print("no file")
          self.timesWentBackInTime = 0
          print(self.timesWentBackInTime)
               
          hist = open(self.historyFile, "a")
          #lines = hist.readlines()
          hist.seek(0)
          hist.write("\n"+self.asdf)
          #for line in lines:
          #     hist.write(line)
          
          #print(self.timesWentBackInTime)

          hist.close()
     def readHistory(self):
          hist = open(self.historyFile)
          self.timesWentBackInTime+=1
          with open(self.historyFile, 'r') as fp:
               lines = len(fp.readlines())
          hist.seek(0)
          e = hist.readlines()
          if self.timesWentBackInTime > lines-2:
               self.timesWentBackInTime-=1
          try:
               #print(e)
               #print(e[lines-(self.timesWentBackInTime)])
               print(self.timesWentBackInTime)
               print(len(e))
               return e[lines-(self.timesWentBackInTime)-1]
          except:
               print("can't go back")
