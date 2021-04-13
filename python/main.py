
from selenium import webdriver
import ctypes
import time
import cv2
import numpy as np

def change(path) :
    dll = ctypes.WinDLL("../background_melon/background_melon.dll")

    changeBackgroundImage = dll["changeBackgroundImage"]
    changeBackgroundImage.argtypes = [ctypes.c_char_p]
    changeBackgroundImage(str(path).encode("utf-8"))

option = webdriver.ChromeOptions()
option.add_argument("headless")
option.add_argument("--disable-gpu")
option.add_argument("lang=ko_KR")

wd = webdriver.Chrome("./chromedriver.exe", chrome_options=option)
wd.get("https://www.melon.com/chart/index.htm")

time.sleep(1)

image = np.array([])

for i in range(1, 4) :
    wd.execute_script("window.scrollTo(0, 430 * " + str(i) + " - " + str(i * 7) + ");")
    wd.save_screenshot("../images/melon" + str(i) + ".png")

    if len(image) == 0 :
        image = cv2.imread("../images/melon" + str(i) + ".png")[:, 50:300]

    else :
        image = np.concatenate((image, cv2.imread("../images/melon" + str(i) + ".png")[:, 50:300]), axis=1)

image = image[50:500]
cv2.imwrite("C:/Users/Public/result.png", image)

ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/Users/Public/result.png" , 0)