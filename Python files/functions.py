#import imports file and mysql library to access database
#libraries imports
from tkinter import *
from tkinter import ttk
from random import choice, randint
from datetime import date, datetime
from string import ascii_uppercase
import tkinter as tk
import pymysql, PIL.Image, ctypes, os
from PIL import ImageTk, Image
from tkinter.ttk import *
import mysql.connector
from time import sleep
import pyautogui
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from datetime import date

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

link = "https://www.autodna.com"

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
errorMsg = "\0"

class Check:
    def __init__(self, vin):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\hp\Desktop\CV2\For CV\CarDealer\Python files\chromedriver_win32\chromedriver.exe",chrome_options=options)
        self.vin = vin
    def xpath_exists(self, xpath):
        driver = self.driver
        try:
            driver.find_element_by_xpath(xpath)
            exist = True
        except NoSuchElementException:
            exist = False
        return exist
    def go_to_page(self):
        driver = self.driver
        driver.get(link)
        if self.xpath_exists("/html/body/div[2]/div[2]/div/div/section/div[2]/form/input[1]"):
            driver.find_element(by = By.XPATH, value = "/html/body/div[2]/div[2]/div/div/section/div[2]/form/input[1]").click()
            pyautogui.write(self.vin)
            if self.xpath_exists("/html/body/div[2]/div[2]/div/div/section/div[2]/form/input[2]"):
                driver.find_element(by = By.XPATH, value ="/html/body/div[2]/div[2]/div/div/section/div[2]/form/input[2]").click()
                sleep(2)
                if self.xpath_exists("/html/body/div[2]/div[2]/div/div/section/div[2]/form/div/p[1]"):
                    return False
                else:
                    return True

def verifyVIN(vin):
    c = Check(vin)
    return c.go_to_page()

#function to connect to database application
def link_xampp(link_button, error_data_base):
    error_data_base.destroy()
    sleep(.1)
    pyautogui.press('win')
    sleep(.1)
    pyautogui.write('Xampp Control Panel')
    sleep(.2)
    pyautogui.press('enter')

def submit_car(info_car, cars, number_cars):
    if len(get_all_children(cars)) < number_cars:
        if len(info_car[0].get()) == 17 and len(info_car[1].get()) in range(9, 11) and int(info_car[2].get()) <= int(date.today().year):
            if verifyVIN(info_car[0].get()):
                cars.insert('', 'end', text="1", values=(info_car[0].get(), info_car[1].get(), info_car[2].get(), info_car[3].get(), info_car[4].get()))
                
def submit_cust(info_cust, cust, number_clients):
    if len(get_all_children(cust)) < number_clients:
        if verifyCNP(info_cust[2].get()):
            cust.insert('', 'end', text="1", values=(info_cust[0].get(), info_cust[1].get(), info_cust[2].get()))

#verification CNP function
def verifyCNP(cnp):
    date = {1:[31,31], 2:[28, 29], 3:[31,31], 4:[30,30], 5:[31,31], 6:[30,30], 7:[31,31], 8:[31,31], 9:[30,30], 10:[31,31], 11:[30,30], 12:[31,31]}
    code = [2,7,9,1,4,6,3,5,8,2,7,9]
    leap = False
    global errorMsg
    if len(cnp) != 13:
        errorMsg = "CNP length wrong"
        return False
    else:
        if int(cnp[3:5]) > 12:
            errorMsg = "Month wrong"
            return False
        else:
            if int(cnp[1:3]) % 4 == 0:
                leap = True
            if (leap and int(cnp[5:7]) > date[int(cnp[3:5])][1]) or (not leap and int(cnp[5:7]) > date[int(cnp[3:5])][0]):
                    errorMsg = "Day wrong"
                    return False
            else:
                if int(cnp[11:13]) < 1 or  int(cnp[11:13]) > 52:
                    errorMsg = "City index wrong"
                    return False
                else:  
                    s = 0
                    cnp = str(cnp)
                    l = [int(c) for c in cnp]
                    for i in range(12):
                        s += l[i]*code[i]
                    if not s % 11 == int(cnp[-1]):
                        errorMsg = "Verification key failed"
                        return False
    return True

#popupMsg function to desplay errors    
def popupMsg(msg, title):
    pop = Tk()
    pop.resizable(height = False, width = False)
    pop.title(title)
    pop.geometry(f"{screensize[0]//4}x{screensize[1]//6}")
    label = ttk.Label(pop, text = msg)
    label.pack(side = "top", pady = 10)
    b = Button(pop, text = "Okay", command = pop.destroy)
    b.pack()
    
#submit_info funtion used in hire() funtion
#to collect infos about the employee
def submit_info(info_employee, data, errorLabel, car_dealer):
    if verifyCNP(info_employee[2].get()):
        errorLabel.config(text = "\0")
        cursor = car_dealer.cursor()
        
        current_time = datetime.now()
        time = current_time.strftime("%H:%M:%S")
        info_employee = [element.get() for element in info_employee]
        if len(info_employee) == 4:
            info_employee.append(str(date.today()))
            info_employee.append(time)
        else:
            info_employee[4] = str(date.today())
            info_employee[5] = time
        if  all(element != '' for element in info_employee):
            list_employee = "INSERT INTO `employee_table`(`Name`, `Surname`, `CNP`, `Salary`, `Date`, `Time`) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(list_employee, info_employee)
            car_dealer.commit()
    else:
        errorLabel.config(text = errorMsg)
    
#submit_cnp function used in fire() function
#to fire a employee(deletion is made by cnp)
def submit_cnp(cnp, car_dealer):
    cursor = car_dealer.cursor()
    delete_employee = "DELETE FROM `employee_table` WHERE CNP = %s"
    cursor.execute(delete_employee, (cnp.get(), ))
    car_dealer.commit()

#get_all_children funtion to get the children
#the Treeview widget 'tree'

def character_limit(entry_text, limit, type, entry):
    if type == "digits" and entry_text.get()[-1] not in "0123456789":
        entry_text.set(entry_text.get()[:-1])
    if type == "chars" and entry_text.get()[-1] in "0123456789":
        entry_text.set(entry_text.get()[:-1])
    if len(entry_text.get()) > 0:
        entry_text.set(entry_text.get()[:limit])

def get_all_children(tree, item=""):
    children = tree.get_children(item)
    for child in children:
        children += get_all_children(tree, child)
    return children

#sell_car funtion that send the car and
#client selected into the database
def sell_car(data_list, car_dealer):
    cursor = car_dealer.cursor()
    add_car = "INSERT INTO `sold_table`(`Car VIN`, `Licence Plate`, `Manuf. Year`, `Brand`, `Model`, `Date`, `Time`, `Verification Code`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    add_cust = "INSERT INTO `custemers_table`(`Name`, `Surname`, `CNP`, `Date`, `Time`, `Verification code`) VALUES (%s, %s, %s, %s, %s, %s)"
    random_list = [str(randint(0,9)) for i in range(6)]
    verification_code = ''
    for i in range(6):
        verification_code += random_list[i]
    data_list[0].append(verification_code)
    data_list[1].append(verification_code)
    data_list[0] = tuple(data_list[0])
    data_list[1] = tuple(data_list[1])
    print(data_list)
    cursor.execute(add_car, data_list[0])
    car_dealer.commit()
    cursor.execute(add_cust, data_list[1])
    car_dealer.commit()
    
#service_list function for the options 
#list from service menu
#selection is made with index
def service_list(index, car_dealer):
    data = Tk()
    data.resizable(height = False, width = False)
    if index == 1:
        data.geometry(f"{screensize[0]//5}x{screensize[1]//4}")
    else:
        data.geometry(f"{screensize[0]//5}x{screensize[1]//8}")
    
    car_vin_label = Label(data, text = "Car VIN: ").grid(row = 0, column = 0)
    car_vin_entry = StringVar()
    car_vin = Entry(data, textvariable = car_vin_entry)
    car_vin.grid(row = 0, column = 1)
    
    licence_plate_label = Label(data, text = "Licence plate: ").grid(row = 1, column = 0)
    licence_plate_entry = StringVar()
    licence_plate = Entry(data, textvariable = licence_plate_entry)
    licence_plate.grid(row = 1, column = 1)
    
    info_cars = [car_vin, licence_plate]
    x_button, y_button = functions.screensize[0]//12, functions.screensize[1]//5
    
    if index == 1:
        details_label = Label(data, text = "Details: ").grid(row = 2, column = 0)
        details = Text(data, height = 5, width = 15)
        details.grid(row = 2, column = 1, sticky = W)
        info_cars.append(details)
        submit = Button(data, text="Submit", command = lambda: service_function(index, info_cars, car_dealer))
    else:
        submit = Button(data, text="Submit", command = lambda: service_function(index, info_cars, car_dealer))
        y_button = functions.screensize[1]//10
    submit.place(x = x_button, y = y_button, anchor = "center")
    
    data.mainloop()

#service_function function to execute commands
#send from service menu
def service_function(index, info_cars, car_dealer):
    cursor = car_dealer.cursor()
    current_time = datetime.now()
    time = current_time.strftime("%H:%M:%S")
    if index != 1:
        info_cars = [info_cars[i].get() for i in range(len(info_cars))]
    else:
        last = info_cars[-1].get("1.0", END)
        info_cars = [info_cars[i].get() for i in range(len(info_cars)-1)]
        info_cars.append(last)
    
    info_cars.append(str(date.today()))
    info_cars.append(time)
    info_cars = tuple(info_cars)
    
    if all(element != '' for element in info_cars):
        if index == 1:
            insert_car = "INSERT INTO `service_table`(`CIV`, `Licence plate`, `Description`, `Date`, `Time`) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(insert_car, info_cars)
        elif index == 2:
            remove_car = "DELETE FROM `service_table` WHERE `CIV` = %s and `Licence plate` = %s"
            cursor.execute(remove_car, info_cars[0:2])
        else:
            data = Tk()
            data.resizable(height = False, width = False)
            search_car = "SELECT * FROM `service_table` WHERE `CIV` = %s and `Licence plate` = %s"
            cursor.execute(search_car, info_cars[0:2])
            result = cursor.fetchall()
            style = ttk.Style(data)
            
            style.theme_use('clam')
            mylist = ttk.Treeview(data, column=("CIV", "Licence plate", "Description", "Date", "Time"), show='headings', height = 1)
            mylist.column("# 1", anchor=CENTER)
            mylist.heading("# 1", text="CIV")
            mylist.column("# 2", anchor=CENTER)
            mylist.heading("# 2", text="Licence plate")
            mylist.column("# 3", anchor=CENTER)
            mylist.heading("# 3", text="Description")
            mylist.column("# 4", anchor=CENTER)
            mylist.heading("# 4", text="Date")
            mylist.column("# 5", anchor=CENTER)
            mylist.heading("# 5", text="Time")
            mylist.pack()
            
            mylist.insert('', 'end', values = (str(result[0][0]), str(result[0][1]), str(result[0][2]), str(result[0][3]), str(result[0][4])))
            
    car_dealer.commit()
    
import functions
from functions import *
#hire function
def hire(car_dealer):
    data = Toplevel()
    data.resizable(height = False, width = False)
    data.geometry(f"{screensize[0]//6}x{screensize[1]//5}")
    
    name_label = Label(data, text = "Name: ").grid(row = 0, column = 0)
    name_entry = StringVar()
    name = Entry(data, textvariable = name_entry)
    name.grid(row = 0, column = 1)
    name_entry.trace("w", lambda *args: character_limit(name_entry, 10, "chars", name))
    
    surname_label = Label(data, text = "Surname: ").grid(row = 1, column = 0)
    surname_entry = StringVar()
    surname = Entry(data, textvariable = surname_entry)
    surname.grid(row = 1, column = 1)
    surname_entry.trace("w", lambda *args: character_limit(surname_entry, 10, "chars", surname))
    
    cnp_label = Label(data, text = "CNP: ").grid(row = 2, column = 0)
    cnp_entry = StringVar()
    cnp = Entry(data, textvariable = cnp_entry)
    cnp.grid(row = 2, column = 1)
    cnp_entry.trace("w", lambda *args: character_limit(cnp_entry, 13, "digits", cnp))
    
    salary_label = Label(data, text = "Salary: ").grid(row = 3, column = 0)
    salary_entry = StringVar()
    salary = Entry(data, textvariable = salary_entry)
    salary.grid(row = 3, column = 1)
    salary_entry.trace("w", lambda *args: character_limit(salary_entry, 5, "digits", salary))
  
    info_employee = [name, surname, cnp, salary]
    
    errorLabel = Label(data, text = "")
    errorLabel.place(x = screensize[0]//12, y = 11*screensize[1]//60, anchor = "center")
    
    submit = Button(data, text="Submit", command = lambda: submit_info(info_employee, data, errorLabel, car_dealer))
    submit.place(x = screensize[0]//12, y = functions.screensize[1]//7, anchor = "center")
    
    data.mainloop()

#fire function    
def fire(car_dealer):
    data = Toplevel()
    data.resizable(height = False, width = False)
    data.geometry(f"{screensize[0]//7}x{screensize[1]//12}")
    
    cnp_label = Label(data, text = "CNP: ").grid(row = 0, column = 0)
    cnp_entry = StringVar()
    cnp = Entry(data, textvariable = cnp_entry)
    cnp.grid(row = 0, column = 1)
    cnp_entry.trace("w", lambda *args: character_limit(cnp_entry, 13, "digits", cnp))

    submit = Button(data, text="Submit", command = lambda: submit_cnp(cnp, car_dealer))
    submit.place(x = screensize[0]//14, y = screensize[0]//28, anchor = CENTER)
    
    data.mainloop()
    
#list function
def list(car_dealer):
    current_time = datetime.now()
    data = Toplevel()
    data.resizable(height = False, width = False)
    #data.geometry("250x100")
    style = ttk.Style(data)
    style.theme_use('clam')
    scrollbar = Scrollbar(data)
    scrollbar.pack(side = RIGHT, fill = Y)
    mylist = ttk.Treeview(data, column=("Name", "Surname", "CNP", "Salary"), show='headings')
    mylist.column("# 1", anchor=CENTER)
    mylist.heading("# 1", text="Name")
    mylist.column("# 2", anchor=CENTER)
    mylist.heading("# 2", text="Surname")
    mylist.column("# 3", anchor=CENTER)
    mylist.heading("# 3", text="CNP")
    mylist.column("# 4", anchor=CENTER)
    mylist.heading("# 4", text="Salary")
    mylist.pack()

    cursor = car_dealer.cursor()

    cursor.execute("SELECT * FROM `employee_table`")
    result = cursor.fetchall()
    for i in range(len(result)):
        mylist.insert('', 'end', values = (str(result[i][0]), str(result[i][1]), str(result[i][2]), str(result[i][3])))
    scrollbar.config(command = mylist.yview)
    
    data.mainloop()
    car_dealer.close()
    
#modify_cars function to modify hights(number of registrations)
#from the cars box
def modify_cars(sign, cars, cars_number_label, number_cars):
    if (number_cars > 1 and sign < 0) or (number_cars < 10 and sign > 0):   
        cars_number_label.config(text = number_cars)
    cars.config(height = number_cars)

#modify_clients function to modify heights
#from the clients box
def modify_clients(sign, cust, clients_number_label,number_clients):
    if (number_clients > 1 and sign < 0) or (number_clients < 10 and sign > 0):  
        clients_number_label.config(text = number_clients)
    cust.config(height = number_clients)
