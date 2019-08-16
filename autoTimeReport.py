'''
 Description:
    Auto make time-sheet report to Segular
 Author:
    nampt282@gmail.com
 Note:
    - python 3.6.8
    - Link: https://www.python.org/downloads/release/python-368/
'''
import pyautogui
import time
import os
import sys
import subprocess
import webbrowser as wb
import json


class locateMouse:
    pic_name,icrs_x,decre_x,icrs_y,decre_y = ["",0,0,0,0]
 
    def assignVal(self,inputList = []):
        self.pic_name = inputList[0]
        self.icrs_x = inputList[1]
        self.decre_x = inputList[2]
        self.icrs_y = inputList[3]
        self.decre_y = inputList[4]
        print(self.pic_name)
   
    def locationOnScreen(self):
        x, y = pyautogui.locateCenterOnScreen(self.pic_name,confidence=0.8)
        x += self.icrs_x
        x -= self.decre_x
        y += self.icrs_y
        y -= self.decre_y
        return x,y
        
    def delay4image(self,imagefile,timeout):
        found_img = None
        while found_img is None and timeout != 0 :
            timeout = timeout - 1
            found_img = pyautogui.locateOnScreen(imagefile, confidence=0.8)
            time.sleep(1)
        
    def leftClick(self,inputList = []):
        self.assignVal(inputList)
        delaytime = 6
        self.delay4image(self.pic_name,delaytime)
        x,y = self.locationOnScreen()
        pyautogui.click(x, y)

def pathof(subdir,filename):
    pathname=os.path.dirname(sys.argv[0]) #current dir of the script
    pathname=os.path.join(pathname,subdir,filename)
    return pathname

def file_get_contents(filename):
    with open(filename, 'r') as f:
        return f.read()


def typewrite_contents(filename,addstr):
    filecontents = file_get_contents(filename) + "\\" + addstr
    print(filecontents)
    pyautogui.typewrite(filecontents)
    time.sleep(2)

def openWebBrowser():
    url="https://px.afdrift.se/login/login.asp"
    wb.open_new_tab(url)
def parseJSONfile():
    with open('data.json', 'r') as f:
        distros_dict = json.load(f)

    for distro in distros_dict:
        print(distro['Database'])

def main():
    #openWebBrowser()
    parseJSONfile()
    #a = locateMouse()
    #a.leftClick([pathof("images","SelectPort.png"), 0, 0, 0, 0])

    
if __name__ == "__main__":
    main()









