from bs4 import BeautifulSoup
import pyautogui
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
optionswindow = Tk()
optionswindow.iconbitmap("resources/pen.ico")
path = StringVar()
def updatevariableinput(*args):
    path.trace_add("write", updatevariableinput)
def program():
    if path.get() == '':
        messagebox.showerror(title="Error", message="You must give some argument in path field")
        return
    print(path.get())
    optionswindow.destroy()
    url = 'https://10fastfingers.com/advanced-typing-test/english'
    option = Options()
    option.add_argument(r"user-data-dir=" + str(path.get()))
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    inputhtml = driver.find_element(By.ID, 'inputfield')
    result = soup.select('[wordnr]')
    for i in result:
        inputhtml.click()
        pyautogui.write(i.text + " ", interval="0.085")
        print(str(i.text))
    input("Press enter to continue...")
    exit()
headerfont = font.Font(family='Arial', size=15, weight="bold")
optionswindow.title("Set path to your chrome")
optionswindow.minsize(250, 250)
text = Label(optionswindow, text="Set your path for user google data", font=headerfont)
undertext = Label(optionswindow, text = "Click windows+r and type \n" + "" + r" %LOCALAPPDATA%\Google\Chrome\User Data\ " + "\n and copy path on the top of explorer window")
input = Entry(optionswindow, textvariable=path, validatecommand=updatevariableinput)
button = Button(optionswindow, text='Ready', command=program)
text.grid(row=0, column=0)
text.pack(anchor=CENTER)
undertext.pack(anchor=CENTER)
input.pack(anchor=CENTER)
button.pack(anchor=CENTER, pady=5)


optionswindow.mainloop()

