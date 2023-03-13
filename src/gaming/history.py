#!/usr/bin/env python3
import os


class history():
     asdf = "bruh"
     timesWentBackInTime = 1
     def __init__(self, p: str):
          self.asdf = p

     def writeHistory(self):
          if self.timesWentBackInTime < 0:
               os.remove("history.txt")
               print("noooooo")
               self.timesWentBackInTime = 0
               pass
               
          else:
               print("yayaya")
               pass
               
          hist = open("history.txt", "a+")
          lines = hist.readlines()
          hist.seek(0)
          hist.write("\n"+self.asdf)
          for line in lines:
               hist.write(line)
          
          print(self.timesWentBackInTime)

          hist.close()
     def readHistory(self):
          hist = open("history.txt", "r")
          self.timesWentBackInTime+=1
          with open(r"history.txt", 'r') as fp:
               lines = len(fp.readlines())
          hist.seek(0)
          e = hist.readlines()
          if self.timesWentBackInTime > lines-2:
               self.timesWentBackInTime-=1
          try:
               print(e)
               print(e[lines-(self.timesWentBackInTime)])
               print(self.timesWentBackInTime)
               print(len(e))
               return e[lines-(self.timesWentBackInTime)]
          except:
               print("can't go back")
