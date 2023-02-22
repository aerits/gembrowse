#!/usr/bin/env python3
import os


class history():
     asdf = "bruh"
     timesWentBackInTime = 0
     def __init__(self, p: str):
          self.asdf = p

     def writeHistory(self):
          self.timesWentBackInTime = 0;
          hist = open("history.txt", "w+")
          lines = hist.readlines()
          hist.seek(0)
          hist.write(self.asdf+"\n")
          for line in lines:
               hist.write(line)

          hist.close()
     def readHistory(self):
          hist = open("history.txt", "r")
          self.timesWentBackInTime+=1
          hist.seek(0)
          e = hist.readlines()
          if self.timesWentBackInTime > len(e)-2:
               self.timesWentBackInTime-=1
          print(e[1+self.timesWentBackInTime])
          print(self.timesWentBackInTime)
          print(len(e))
          return e[1+self.timesWentBackInTime]
