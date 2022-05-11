#import all from imports file
from functions import *
                    
#create Window class
class Window(Frame):
    #define constructor
    def __init__(self, master, number_cars, number_clients, car_dealer):
    
        #initialize class's attributes
        Frame.__init__(self, master)
        self.master, self.number_cars, self.number_clients, self.car_dealer = master, number_cars, number_clients, car_dealer

        #add a Treeview widget
        cars = ttk.Treeview(root, column=("VIN", "LPlate", "ManYear", "Brand", "Model"), show='headings', height = self.number_cars)
        cars.column("# 1", anchor=CENTER)
        cars.heading("# 1", text="Car VIN")
        cars.column("# 2", anchor=CENTER)
        cars.heading("# 2", text="License Plate")
        cars.column("# 3", anchor=CENTER)
        cars.heading("# 3", text="Manuf. Year")
        cars.column("# 4", anchor=CENTER)
        cars.heading("# 4", text="Brand")
        cars.column("# 5", anchor=CENTER)
        cars.heading("# 5", text="Model")
        cars.pack(fill = "both")

        #add a Treeview widget
        cust = ttk.Treeview(root, column=("FName", "LName", "CustID"), show='headings', height = self.number_clients)
        cust.column("# 1", anchor=CENTER)
        cust.heading("# 1", text="First Name")
        cust.column("# 2", anchor=CENTER)
        cust.heading("# 2", text="Last Name")
        cust.column("# 3", anchor=CENTER)
        cust.heading("# 3", text="CNP")
        cust.pack(fill = "both")

        #create main menu
        menu = Menu(self.master)
        self.master.config(menu = menu)

        #file menu
        fileMenu = Menu(menu)
        fileMenu.add_command(label="Change heights", command = lambda: self.changeHeights(cars, cust))
        fileMenu.add_command(label="Exit", command = self.exitProgram)
        menu.add_cascade(label="File", menu = fileMenu)

        #edit menu
        editMenu = Menu(menu)
        menu.add_cascade(label="Edit", menu=editMenu)
        editMenu_car = Menu(editMenu, tearoff = 0)
        editMenu_car.add_command(label = 'Buy car', command = lambda: self.addCar(cars))
        editMenu_car.add_command(label = 'Sell car', command = lambda: self.sellCar(cars, cust))
        editMenu_car.add_command(label = 'Remove car', command = lambda: self.delCar(cars))
        
        #submenu of edit menu
        editMenu_customer = Menu(editMenu, tearoff = 0)
        editMenu_customer.add_command(label = 'Add customer', command = lambda: self.addCust(cust))
        editMenu_customer.add_command(label = 'Remove customer', command = lambda: self.delCust(cust))
        editMenu.add_cascade(label = 'Car', menu = editMenu_car)
        editMenu.add_cascade(label = 'Customer', menu = editMenu_customer)

        #staff menu
        staffMenu = Menu(menu)
        staffMenu.add_command(label="Hire employee", command = lambda: hire(self.car_dealer))
        staffMenu.add_command(label="Fire employee", command = lambda: fire(self.car_dealer))
        staffMenu.add_command(label="List employees", command = lambda: list(self.car_dealer))
        menu.add_cascade(label = "Staff", menu = staffMenu)
        
        #service menu
        service = Menu(menu)
        service.add_command(label="Add in service", command = lambda: service_list(1, self.car_dealer))
        service.add_command(label="Remove from service", command = lambda: service_list(2, self.car_dealer))
        service.add_command(label="Search in service", command = lambda: service_list(3, self.car_dealer))
        menu.add_cascade(label = "Service", menu = service)

    #exit function
    def exitProgram(self):
        ask = Toplevel()
        ask.resizable(height = False, width = False)
        ask.geometry(f"{screensize[0]//5}x{screensize[1]//7}+{3*screensize[0]//10}+{5*screensize[1]//14}")
        
        ask_label = Label(ask, text = "\tAre you sure\n \tyou want to exit ?\n")
        ask_label.grid(column = 0, row = 0)
        
        yes_button = Button(ask, text="Yes",  command = exit)
        yes_button.grid(column = 0, row = 1)
        
        no_button = Button(ask, text="No", command = ask.destroy)
        no_button.grid(column = 1, row = 1)
        
        ask.mainloop()

    #addCar function
    def addCar(self, cars):
        
            today = str(date.today()).split('-')
            current_year = int(today[0])
            data = Toplevel()
            data.resizable(height = False, width = False)
            data.geometry(f"{screensize[0]//4}x{screensize[1]//3}")
    
            vin_label = Label(data, text = "Car VIN: ").place(x = 0, y = screensize[1]//40)
            vin_entry = StringVar()
            vin = Entry(data, textvariable = vin_entry)
            vin.place(x = screensize[0]//8, y = screensize[1]//40)
            vin.focus_set()
            vin_entry.trace("w", lambda *args: character_limit(vin_entry, 17, "text", vin))
            
            license_label = Label(data, text = "License Plate: ").place(x = 0, y = 3*screensize[1]//40)
            license_entry = StringVar()
            license = Entry(data, textvariable = license_entry)
            license.place(x = screensize[0]//8, y = 3*screensize[1]//40)
            license_entry.trace("w", lambda *args: character_limit(license_entry, 9, "text", license))
            
            year_label = Label(data, text = "Manuf. year: ").place(x = 0, y = 5*screensize[1]//40)
            year_entry = StringVar()
            year = Entry(data, textvariable = year_entry)
            year.place(x = screensize[0]//8, y = 5*screensize[1]//40)
            year_entry.trace("w", lambda *args: character_limit(year_entry, 4, "digits", year))
            
            brand_label = Label(data, text = "Brand: ").place(x = 0, y = 7*screensize[1]//40)
            brand_entry = StringVar()
            brand = Entry(data, textvariable = brand_entry)
            brand.place(x = screensize[0]//8, y = 7*screensize[1]//40)
            brand_entry.trace("w", lambda *args: character_limit(brand_entry, 10, "text", brand))
            
            model_label = Label(data, text = "Model: ").place(x = 0, y = 9*screensize[1]//40)
            model_entry = StringVar()
            model = Entry(data, textvariable = model_entry)
            model.place(x = screensize[0]//8, y = 9*screensize[1]//40)
            model_entry.trace("w", lambda *args: character_limit(model_entry, 10, "text", model))
            
            info_car = [vin, license, year, brand, model]
        
            style = Style()
            style.configure('W.TButton', font = ('calibri', 10, 'bold', 'underline'), foreground = 'red')
        
            submit = Button(data, text="Submit", command = lambda: submit_car(info_car, cars, self.number_cars))
            submit.place(x = screensize[0]//8, y = 12*screensize[1]//40, anchor = "center")
            
            data.mainloop()

    #sellCar function
    def sellCar(self, cars, cust):
        try:
            selected_car  = cars.selection()[0]
            selected_cust = cust.selection()[0]
        except IndexError:
            popupMsg("Please select one car and one customer", "Car selection ERR")
        else:
            data_list_car = cars.item(selected_car)['values']
            data_list_cust = cust.item(selected_cust)['values']
            cars.delete(selected_car)
            cust.delete(selected_cust)
            data_list_car = [str(element) for element in data_list_car]
            data_list_cust = [str(element) for element in data_list_cust]
            data_list_car.append(str(date.today()))
            data_list_cust.append(str(date.today()))
            current_time = datetime.now()
            time = current_time.strftime("%H:%M:%S")
            data_list_car.append(time)
            data_list_cust.append(time)
            data_list = [data_list_car, data_list_cust]
            sell_car(data_list, self.car_dealer)

    #addCust function
    def addCust(self, cust):
        data = Toplevel()
        data.resizable(height = False, width = False)
        data.geometry(f"{screensize[0]//6}x{screensize[1]//5}")

        name_label = Label(data, text = "Name: ").grid(row = 0, column = 0, sticky = W)
        name_entry = StringVar()
        name = Entry(data, textvariable = name_entry)
        name.grid(row = 0, column = 1)
        name_entry.trace("w", lambda *args: character_limit(name_entry, 10, "chars", name))
        
        surname_label = Label(data, text = "Surname: ").grid(row = 1, column = 0, sticky = W)
        surname_entry = StringVar()
        surname = Entry(data, textvariable = surname_entry)
        surname.grid(row = 1, column = 1)
        surname_entry.trace("w", lambda *args: character_limit(surname_entry, 10, "chars", surname))
        
        cnp_label = Label(data, text = "CNP: ").grid(row = 2, column = 0, sticky = W)
        cnp_entry = StringVar()
        cnp = Entry(data, textvariable = cnp_entry)
        cnp.grid(row = 2, column = 1)
        cnp_entry.trace("w", lambda *args: character_limit(cnp_entry, 13, "digits", cnp))
        
        info_cust = [name, surname, cnp]
        
        submit = Button(data, text="Submit", command = lambda: submit_cust(info_cust, cust, self.number_clients))
        submit.place(x = screensize[0]//12, y = screensize[1]//6, anchor = "center")
        
        
        data.mainloop()

    #delCust function
    def delCust(self, cust):
        try:
            selected_item = cust.selection()[0]
        except IndexError:
            popupMsg("Please select one customer", "Customer selection ERR")
        else:
            cust.delete(selected_item)
            
    #delCust function
    def delCar(self, cars):
        try:
            selected_item = cars.selection()[0]
        except IndexError:
            popupMsg("Please select one car", "Car selection ERR")
        else:
            cars.delete(selected_item)

    #changeHeights funtion
    def changeHeights(self, cars, cust):
        global number_cars, number_clients 
          
        change = Toplevel()
        change.resizable(height = False, width = False)
        change.title("Modify")
        change.geometry(f"{screensize[0]//8}x{screensize[1]//8}+{7*screensize[0]//16}+{7*screensize[1]//16}")
        
        cars_label = Label(change, text = "Cars")
        cars_label.grid(column=0,row=0)
        cars_number_label = Label(change, text = self.number_cars)
        cars_number_label.grid(column=1,row=0)

        clients_label = Label(change, text = "Clients")
        clients_label.grid(column=0,row=2)
        clients_number_label = Label(change, text = self.number_clients)
        clients_number_label.grid(column=1,row=2)
        
        button_cars_plus = Button(change, text="Add", command = lambda: [add_cars(self), modify_cars(1, cars, cars_number_label, self.number_cars)])
        button_cars_plus.grid(column = 0, row = 1)

        button_cars_minus = Button(change, text="Remove", command = lambda: [del_cars(self), modify_cars(-1, cars, cars_number_label, self.number_cars)])
        button_cars_minus.grid(column = 1, row = 1)

        button_client_plus = Button(change, text="Add", command = lambda: [add_cust(self), modify_clients(1, cust, clients_number_label, self.number_clients)])
        button_client_plus.grid(column = 0, row = 3)

        button_client_minus = Button(change, text="Remove", command = lambda: [del_cust(self), modify_clients(-1, cust, clients_number_label, self.number_clients)])
        button_client_minus.grid(column = 1, row = 3)
        
        def add_cars(self):
            if self.number_cars <= 50 - self.number_clients:
                self.number_cars += 1
         
        def del_cars(self):
            if self.number_cars > len(get_all_children(cars)):
                self.number_cars -= 1

        def add_cust(self):
            if self.number_clients <= 50 - self.number_cars:
                self.number_clients += 1
                
        def del_cust(self):
            if self.number_clients > len(get_all_children(cust)):
                self.number_clients -= 1
        
        change.mainloop()
        
#main function
if __name__ == "__main__":
    try:
        #create a database variable
        car_dealer = mysql.connector.connect(
            user = "root",
            password = "",
            host="localhost",
            database = "car_dealer"
        )  
        number_cars, number_clients = 16, 16
        root = Tk()
        app = Window(root, number_cars, number_clients, car_dealer)
        root.wm_title("Car Dealer 0.0.2")
        root.attributes("-fullscreen", True)
        #create an object of Style widget
        style = ttk.Style()
        style.theme_use('clam')
        root.mainloop()
        
    except:
        error_data_base = Tk()
        width1, height1 = 600, 600
        image1 = PIL.Image.open("./data_base_wallpaper.png")
        resized1 = image1.resize((width1, height1))
        wallpaper_image = ImageTk.PhotoImage(resized1)
        label_wallpaper = Label(error_data_base, image = wallpaper_image)
        label_wallpaper.pack()
        
        image2 = PIL.Image.open("./arrow_button.png")
        resized2 = image2.resize((100, 80))
        arrow_image = ImageTk.PhotoImage(resized2)
        
        link_button = Button(error_data_base, image = arrow_image, text = "Go to Xampp \nControl Panel", compound = "bottom")
        link_button.place(x = width1-130, y = 10, width = 120, height = 140)
        link_button.configure(command = lambda: link_xampp(link_button, error_data_base))
        posX, posY = screensize[0]//2-width1//2, screensize[1]//2-height1//2
        error_data_base.geometry(f"{width1}x{height1}+{posX}+{posY}")
        error_data_base.resizable(False, False)
        error_data_base.mainloop()
    
    
    