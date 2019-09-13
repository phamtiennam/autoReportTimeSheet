'''
 Description:
    Auto make time-sheet report to Segular
 Author:
    nampt282@gmail.com
 Note:
    - python 3.6.8
    - Link: https://www.python.org/downloads/release/python-368/
 Dependcies:
    sudo apt-get install scrot
    pip install opencv-python
'''
import pyautogui
import time
import os
import sys
import subprocess
import webbrowser as wb
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

jsonfile='data.json'
url = "https://px.afdrift.se/login/login.asp"


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
        delaytime = 15
        self.delay4image(self.pic_name,delaytime)
        x,y = self.locationOnScreen()
        pyautogui.click(x, y)
        print("......")

    def fill_in_text(self,strData, inputList = []):
        self.leftClick(inputList)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.typewrite(strData)


def pathof(subdir,filename):
    pathname=os.path.dirname(sys.argv[0]) #current dir of the script
    pathname=os.path.join(pathname,subdir,filename)
    return pathname

def getValFromJasonFile(key,jsonfile):
    with open(jsonfile, 'r') as f:
        data_dict = json.load(f)
    for data in data_dict:
        return data[key]

def main():
    a = locateMouse()

    #openWebBrowser
    driver = webdriver.Chrome()
    #driver.maximize_window()
    driver.set_window_size(1080,800)
    driver.implicitly_wait(30)
    driver.get(url)

    #Login
    elem = driver.find_element_by_id("username")
    elem.send_keys(getValFromJasonFile('Username',jsonfile))

    elem = driver.find_element_by_id("password")
    elem.send_keys(getValFromJasonFile('Password',jsonfile))

    elem = driver.find_element_by_name("server")
    elem.send_keys(getValFromJasonFile('Server',jsonfile))

    elem = driver.find_element_by_name("database")
    elem.send_keys(getValFromJasonFile('Database',jsonfile))

    time.sleep(5)

    elem.send_keys(Keys.RETURN)

    

    #Click on Välj Button
    a.leftClick([pathof("images","valjButton.png"), 0, 0, 0, 0])

    #Click on OK Button
    counter=15
    ok_button = None
    while ok_button is None and counter != 0 :
        counter = counter - 1
        ok_button = pyautogui.locateOnScreen(pathof("images","okButton.png"), confidence=0.8)
        time.sleep(1)
   
    if ok_button is not None:
        a.leftClick([pathof("images","okButton.png"), 0, 0, 0, 0])


    #Activity and Assignment ID
    a.fill_in_text(getValFromJasonFile('Activity',jsonfile),[pathof("images","Activity.png"), 0, 0, 30, 0])
    a.fill_in_text(getValFromJasonFile('Assignment',jsonfile),[pathof("images","Assignment.png"), 0, 0, 30, 0])
    a.leftClick([pathof("images","load.png"), 0, 0, 0, 0])

    #Working Days
    week = ["Mon", "Tues", "Wed", "Thurs", "Fri"]
    for date in week:
        imagefile= date + ".png"
        val=getValFromJasonFile(date,jsonfile)
        if "0" in val or val.isdigit() is False:
             a.fill_in_text("8",[pathof("images",imagefile), 0, 10, 30, 0])
        else:
            a.fill_in_text(val,[pathof("images",imagefile), 0, 10, 50, 0])

    pyautogui.alert(text='Please check and save the time-sheet then Click OK when you are done', title='', button='OK')

    print("_____________END_____________________")

if __name__ == "__main__":
    main()









