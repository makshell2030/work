from tkinter import * # imports tkinter module
import socket # imports socket module
from netmiko import ConnectHandler # imports netmiko
import time # imports date and time
import requests # imports request

net_connect = ConnectHandler(  # assigns the connection details to the user
    device_type="linux", #type of the device
    host="127.0.0.1", # ip address of the host
    port="5679", #  port of the connection
    username="devasc", # log in username
    password="root", # password for a log in
)


window = Tk() # sets window as tk command 

def retrieve_date(): # defines a function to get date
        print("The date and time on the device is ", time.ctime()) # prints the result

def retrieve_ip(): # defines a function to get IP
        name=socket.gethostname()   # sets name to be host
        IP=socket.gethostbyname(name) # gets IP
        print("The IP address of the device is: "+IP)# returns the IP

def retrieve_ls():# defines a function to list the directories
        command = "ls" # sets the command for the terminal
        output = net_connect.send_command(command) # sends the command to the remote desktop
        print("Folders in the remote directory are:", output) # returns the result

def retrieve_backup():# defines a function to back up
        file = str(input("Enter the file ")) # enter the name of the file
        command = "cp "+ file +" test.txt.old" ; #command to copy the file with a new name
        output = net_connect.send_command(command) # sends the command to the remote desktop
        print("The backup file is created") # prints the value

def webpage(): # defines a function to save the webpage
        host=input(str("Please enter the website host ")) # asks the user for the input
        headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'  # defines a user agent used to simulate a browser
        }
        response = requests.get(url=host, headers=headers) # requests a http website
        page = response.text # saves the response as a html
        file_html = open("html.txt", "w") # opens a file 
        file_html.write(page) # writes the html into the file
        file_html.close() #closes the file 
        print("Successful") # shows that the request was successful
        try : # in case of the error caused by connection to the webpage it will print the message and run the script again
                response = requests.get(url=host, headers=headers) # requests a http website
        except:
                print("Try different website") # message
                webpage() # runs the script

while True: # sets a while loop
    window.title("Software") # assigns a name of a window
    window.configure(width=500, height=300) # configures the size of the window
    window.configure(bg='lightgray') # sets the colour
    winWidth = window.winfo_reqwidth() # automatically determines the width as the windows screen
    winwHeight = window.winfo_reqheight()# automatically determines the height as the windows screen
    posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2) # automatically positions the window as the windows screen
    posDown = int(window.winfo_screenheight() / 2 - winwHeight / 2)# automatically positions the window as the windows screen
    window.geometry("+{}+{}".format(posRight, posDown))# correctly formats the position of the window using the preset positions

   
    T = Text(window, height = 5, width = 52) # sets the size for the text window
    l = Label(window, text = "Options") # sets the size of the lable
    l.config(font =("Courier", 14)) # sets the font for the lable
 
    Option = """1 - Show date and time (local computer)""" #options presented to the user
    Option1 = """2 - Show IP address (local computer)"""#options presented to the user
    Option2 = """3 - Show Remote home directory listing"""#options presented to the user
    Option3 = """4 - Backup remote file"""#options presented to the user
    Option4 = """5 - Save web page"""#options presented to the user
    Option5 = """Q - Quit"""#options presented to the user
    space= "\n" # prints a space 

    
    
    b1 = Button(window, text = "Option 1" ,
                command = retrieve_date) # Button with the first option to retrieve date of the remote computer.
    b2 = Button(window, text = "Option 2" ,
                command = retrieve_ip) # Button with the second option to retrieve ip of the remote computer.
    b3 = Button(window, text = "Option 3" ,
                command = retrieve_ls) # Button with the third option to list the directories of the home folder of the remote computer.
    b4 = Button(window, text = "Option 4" ,
                command = retrieve_backup)# Button with the fourth option to create a backup file on the remote computer.
    b5 = Button(window, text = "Option 5" ,
                command = webpage) # Button with the fith option to save HTML of the webpage in the file.
    b6 = Button(window, text = "Exit",
                command = window.destroy) # Last button to exit the code


    l.pack() # calls the widget
    T.pack()# calls the widget
    b1.pack()# calls the widget
    b2.pack()# calls the widget
    b3.pack()# calls the widget
    b4.pack()# calls the widget
    b5.pack()# calls the widget
    b6.pack()# calls the widget
    
    
    

 
    # Insert The Fact.
    T.insert('end', Option) # adds the text to the text widget
    T.insert('end', space)# adds the text to the text widget
    T.insert('end', Option1)# adds the text to the text widget
    T.insert('end', space)# adds the text to the text widget
    T.insert('end', Option2)# adds the text to the text widget
    T.insert('end', space)# adds the text to the text widget
    T.insert('end', Option3)# adds the text to the text widget
    T.insert('end', space)# adds the text to the text widget
    T.insert('end', Option4)# adds the text to the text widget
    T.insert('end', space)# adds the text to the text widget
    T.insert('end', Option5)# adds the text to the text widget


    
    

    window.mainloop()# calls the mainloop






