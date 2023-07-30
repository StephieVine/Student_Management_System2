import os
import tempfile
from tkinter import *
from PIL import Image, ImageTk
import time
import datetime as dt
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
import datetime



windows=Tk()
windows.geometry('1290x800+0+0')
windows.config(bg='cadet blue')
windows.title('Management Project')

def time_update():
    currenttime= time.strftime("%H:%M:%S")
    crnt_time.config(text=currenttime) #display the given time format
    crnt_time.after(1000, time_update) #update the time after every 1000 secs

date=dt.datetime.now()

currentDateTime = datetime.datetime.now()

def upload():
    global filename

    filename=filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image File',
                                        filetypes=(("JPG file", ".jpg"), ("PNG file", ".png"),
                                                   ("All files", ".txt"))) #parameter for files format
    img=(Image.open(filename)) #to open the selected file
    image_resize=img.resize((220, 220)) #return a resized copy of the image
    selected_Image=ImageTk.PhotoImage(image_resize) #is to make the image compartible with tkinter
    lbl.config(image=selected_Image) #to configure the selected image
    lbl.image=selected_Image #to attach the selected image on the created label frame
    img.save("C:\\Users\\Igbon Ifijeh\\Desktop\\School_Management_Project/"+ str(selected_Image) + ".jpg")

def register():
    global img, connect

    #validations: if statement to condition the fields
    if id_entryname.get() == '' or firstnameEntry.get() == '' or lastnameEntry.get() == '' or dobEntry.get() == ''\
        or religionEntry.get() == '' or class_1Entry.get() == ''or fatherNameEntry.get() == ''\
        or motherNameEntry.get() == '' or homeaddressEntry.get() == '' or gender.get() == '' or variable1.get() == ''\
        or phone_noEntry.get() == '' or nokEntry.get() == '' or phone_noEntry.get() == '':
        messagebox.showerror("!", "Please ensure data have been entered on all fields")
        return

    else:
        studentDetailsText.insert(END, '\t\t\**********Student\'s Information*******' + '\n')
        studentDetailsText.insert(END, "Student Registration No: \t\t\t\t" + id_entryname.get() + "\n")
        studentDetailsText.insert(END, "                                                        " + "\n")
        studentDetailsText.insert(END, "First Name: \t\t\t\t" + firstnameEntry.get() + "\n")
        studentDetailsText.insert(END, "                                                        " + "\n")
        studentDetailsText.insert(END, "Last Name: \t\t\t\t" + lastnameEntry.get() + "\n")
        studentDetailsText.insert(END, "                                                        " + "\n")
        studentDetailsText.insert(END, "Date of Birth: \t\t\t\t" + dobEntry.get() + "\n")
        studentDetailsText.insert(END, "                                                        " + "\n")
        studentDetailsText.insert(END, "Religion: \t\t\t\t" + religionEntry.get() + "\n")
        studentDetailsText.insert(END, "                                                        " + "\n")
        studentDetailsText.insert(END, "Class: \t\t\t\t" + class_1Entry.get() + "\n")
        studentDetailsText.insert(END, "                                                        " + "\n")
        studentDetailsText.insert(END, "Father\'s Name: \t\t\t\t" + firstnameEntry.get() + "\n")
        studentDetailsText.insert(END, "                                                        " + "\n")
        studentDetailsText.insert(END, "Mother\'s Name: \t\t\t\t" + motherNameEntry.get() + "\n")
        studentDetailsText.insert(END, "                                                        " + "\n")
        studentDetailsText.insert(END, "Home Address: \t\t\t\t" + homeaddressEntry.get() + "\n")
        studentDetailsText.insert(END, "                                                        " + "\n")
        studentDetailsText.insert(END, "Gender: \t\t\t\t" + gender.get() + "\n")
        studentDetailsText.insert(END, "                                                        " + "\n")
        studentDetailsText.insert(END, "Country: \t\t\t\t" + variable1.get() + "\n")
        studentDetailsText.insert(END, "                                                        " + "\n")
        studentDetailsText.insert(END, "Phone Number: \t\t\t\t" + phone_noEntry.get() + "\n")
        studentDetailsText.insert(END, "                                                        " + "\n")
        studentDetailsText.insert(END, "Name of Next of Kin: \t\t\t\t" + nokEntry.get() + "\n")
        studentDetailsText.insert(END, "                                                        " + "\n")
        studentDetailsText.insert(END, "Phone Number of Next of Kin: \t\t\t\t" + phone_nokEntry.get() + "\n")
        studentDetailsText.insert(END, "*************END*************"+ "\n")

    #database connection
    connect=sqlite3.connect("Student_Management_Project.db", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    cursor = connect.cursor()

    connect.execute("CREATE TABLE IF NOT EXISTS Student_Management_Project_Table(Student_Id TEXT NOT NULL, "
                    "First_Name TEXT NOT NULL, Last_Name TEXT NOT NULL, Date_Of_Birth TEXT NOT NULL, "
                    "Religion TEXT NOT NULL, Class TEXT NOT NULL, Father_Name TEXT NOT NULL, "
                    "Mother_Name TEXT NOT NULL, Home_Address TEXT NOT NULL, Gender TEXT NOT NULL, "
                    "Country TEXT NOT NULL, Phone_Number TEXT NOT NULL, Name_Of_Next_Of_Kin TEXT NOT NULL, "
                    "Phone_Number_of_Next_Of_Kin TEXT NOT NULL, Time_Stamp TIMESTAMP)")
    cursor.execute("SELECT * FROM Student_Management_Project_Table")
    # print("Table created succesfully")
    # messagebox.showinfo("!","Database created")
    # connect.commit() #changes should be made to the connection
    # connect.close()

    selection = ("SELECT * FROM Student_Management_Project_Table WHERE Student_Id = ?")
    cursor.execute(selection, [(id_entryname.get())])
    if cursor.fetchone():
        id_entryname.delete(0, END)
        firstnameEntry .delete(0, END)
        lastnameEntry .delete(0, END)
        dobEntry .delete(0, END)
        religionEntry .delete(0, END)
        class_1Entry .delete(0, END)
        fatherNameEntry .delete(0, END)
        motherNameEntry.delete(0, END)
        homeaddressEntry.delete(0, END)
        gender.set(0)
        variable1.set("Select Country")
        phone_noEntry.delete(0, END)
        nokEntry.delete(0, END)
        phone_nokEntry.delete(0, END)
        studentDetailsText.delete("1.0", END)
        registerbtn.config(state="normal")
        Image1=PhotoImage(file="admin image.png")
        lbl.config(image=Image1)
        lbl.image=Image1
        img = ""
        messagebox.showerror("!", "ID already exist")
        return
    else:
        insert = str("INSERT INTO Student_Management_Project_Table(Student_Id,First_Name,Last_Name,"
                     "Date_Of_Birth,Religion, Class, Father_Name, Mother_Name, Home_Address, Gender, Country,"
                     "Phone_Number, Name_Of_Next_Of_Kin, Phone_Number_of_Next_Of_Kin, Time_Stamp) "
                     "VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)")
        cursor.execute(insert, (id_entryname.get(), firstnameEntry.get(), lastnameEntry.get(), dobEntry.get(),
                                religionEntry.get(), class_1Entry.get(), fatherNameEntry.get(), motherNameEntry.get(),
                                homeaddressEntry.get(), gender.get(), variable1.get(), phone_noEntry.get(),
                                nokEntry.get(), phone_nokEntry.get(), currentDateTime))
        messagebox.showinfo("Success", "Successful storage")
        connect.commit()
        connect.close()

def reset():
    id_entryname.delete(0, END)
    firstnameEntry.delete(0, END)
    lastnameEntry.delete(0, END)
    dobEntry.delete(0, END)
    religionEntry.delete(0, END)
    class_1Entry.delete(0, END)
    fatherNameEntry.delete(0, END)
    motherNameEntry.delete(0, END)
    homeaddressEntry.delete(0, END)
    gender.set(0)
    variable1.set("Select Country")
    phone_noEntry.delete(0, END)
    nokEntry.delete(0, END)
    phone_nokEntry.delete(0, END)
    studentDetailsText.delete("1.0", END)
    registerbtn.config(state="normal")
    Image1 = PhotoImage(file="admin image.png")
    lbl.config(image=Image1)
    lbl.image = Image1
    img = ""

def exit():
    exit=messagebox.askyesno('!', "Do you want to exit?")
    if exit:
        windows.destroy()


def print(txt):
    printquestion=messagebox.askyesno("?", "Do you want to print the details?")
    if printquestion:
        temp_file = tempfile.mktemp(".txt")
        open(temp_file, 'w').write(txt)
        os.startfile(temp_file, 'print')


#variable for data collection
id_entryname=IntVar()
firstnameEntry=StringVar()
lastnameEntry=StringVar()
dobEntry=StringVar()
religionEntry=StringVar()
class_1Entry=StringVar()
fatherNameEntry=StringVar()
motherNameEntry=StringVar()
homeaddressEntry=StringVar()
gender=StringVar()
variable1=StringVar()
phone_noEntry=StringVar()
nokEntry=StringVar()
phone_nokEntry=StringVar()


#Label for profile name
prflname=Label(windows, text="Student\'s Management", font=('tahoma', 18, 'bold'), bg='cadet blue')
prflname.place(x=454, y=0)

prflname2=Label(windows, text="System", font=('tahoma', 18, 'bold'), bg='cadet blue')
prflname2.place(x=530, y=40)

#Student frames

data_frame1= LabelFrame(windows, bd=7, bg='cadet blue', font=('Harrington', 13, 'bold'), width=450,
                        height=670, relief=GROOVE)
data_frame1.place(x=2, y=20)

nok_frame=LabelFrame(data_frame1, bd=7, text='Next of Kin', font=('ariel', 10, 'bold'),
                     bg='cadet blue', width=430, height=80)
nok_frame.place(x=2, y=570)

studentDetails_frame=LabelFrame(windows, bd=7, bg='cadet blue',text='Student details', font=('Harrington', 13, 'bold'),
                                width=450, height=670, relief=GROOVE)
studentDetails_frame.place(x=740, y=20)

studentDetailsText=Text(studentDetails_frame, height=28, width=63, bd=5, bg='white', font=('arield', 11, 'bold'))
studentDetailsText.grid(row=0, column=0)

#button frame
button_frame= LabelFrame(windows,bd=7, bg='cadet blue',width=530, height=120)
button_frame.place(x=740, y=570)

#image frame
image_frame=Frame(windows, bd=3, bg='black', width=230, height=230, relief=GROOVE)
image_frame.place(x=480, y=100)

img=PhotoImage(file='admin image.png')
lbl=Label(image_frame, bg='white', image=img)
lbl.place(x=0, y=0)

gender=StringVar()
variable1=StringVar()


#Labels and Entry fields

student_Id = Label(data_frame1, text='Student\'s ID:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black')
student_Id.place(x=2, y=10)

id_entryname=Entry(data_frame1, width=30, borderwidth=3, font=('tahoma',10))
id_entryname.place(x=200, y=11)

firstname=Label(data_frame1,text='First Name:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
firstname.place(x=2, y=60)

firstnameEntry=Entry(data_frame1, width=30, borderwidth=3, font=('tahoma',10))
firstnameEntry.place(x=200, y=61)

lastname=Label(data_frame1,text='Last Name:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
lastname.place(x=2, y=110)

lastnameEntry=Entry(data_frame1, width=30, borderwidth=3, font=('tahoma',10))
lastnameEntry.place(x=200, y=111)

dob=Label(data_frame1,text='DOB:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
dob.place(x=2, y=160)

dobEntry=Entry(data_frame1, width=30, borderwidth=3, font=('tahoma',10))
dobEntry.place(x=200, y=161)

religion=Label(data_frame1,text='Religion:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
religion.place(x=2, y=210)

religionEntry=Entry(data_frame1, width=30, borderwidth=3, font=('tahoma',10))
religionEntry.place(x=200, y=211)

class_1=Label(data_frame1,text='Class:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
class_1.place(x=2, y=260)

class_1Entry=Entry(data_frame1, width=30, borderwidth=3, font=('tahoma',10))
class_1Entry.place(x=200, y=261)

fatherName=Label(data_frame1,text='Father\'s Name:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
fatherName.place(x=2, y=310)

fatherNameEntry=Entry(data_frame1, width=30, borderwidth=3, font=('tahoma',10))
fatherNameEntry.place(x=200, y=311)

motherName=Label(data_frame1,text='Mother\'s Name:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
motherName.place(x=2, y=360)

motherNameEntry=Entry(data_frame1, width=30, borderwidth=3, font=('tahoma',10))
motherNameEntry.place(x=200, y=361)

homeaddress=Label(data_frame1,text='Home Address:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
homeaddress.place(x=2, y=410)

homeaddressEntry=Entry(data_frame1, width=30, borderwidth=3, font=('tahoma',10))
homeaddressEntry.place(x=200, y=411)

gender.set(0)
genderLabel=Label(data_frame1, text='Gender:', fg='black', bg='cadet blue', font=('tahoma', 13, 'bold'))
genderLabel.place(x=2, y=450)

genderRadio1=Radiobutton(data_frame1, bg='cadet blue', text='Male', variable=gender,
                         value='Male', font=('tahoma', 13, 'bold'))
genderRadio1.place(x=200, y=450)

genderRadio2=Radiobutton(data_frame1, bg='cadet blue', text='Female', variable=gender,
                         value='Female', font=('tahoma', 13, 'bold'))
genderRadio2.place(x=290, y=450)

#country selection
countryLabel=Label(data_frame1, text='Country:', fg='black', bg='cadet blue', font=('tahoma', 13, 'bold'))
countryLabel.place(x=2, y=490)

countries=['ALgeria', 'Australia','Bahamas','Canada', 'Denmark', 'Egypt', 'France', 'Finland', 'Germany',
           'Holland', 'Hungary', 'Indonesia', 'Jamaica', 'Libya','Malaysia', 'Nigeria', 'Poland', 'Qatar', 'Russia',
           'Senegal', 'Uruguay', 'Venezuela']

variable1.set('Select Country')

countryLabelDropdown=OptionMenu(data_frame1, variable1, *countries)
countryLabelDropdown.place(x=200, y=490)

countryLabelDropdown.config(width=15, font=('tahoma', 13, 'bold'), fg='black')


phone_no=Label(data_frame1,text='Phone No:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
phone_no.place(x=2, y=530)

phone_noEntry=Entry(data_frame1, width=30, borderwidth=3, font=('tahoma',10))
phone_noEntry.place(x=200, y=531)

#Next of kin
nok=Label(nok_frame,text='Next of Kin:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
nok.place(x=2, y=2)

nokEntry=Entry(nok_frame, width=30, borderwidth=3, font=('tahoma',10))
nokEntry.place(x=195, y=2)

phone_nok=Label(nok_frame,text='Phone No:', font=('tahoma', 13, 'bold'), bg='cadet blue', fg='black' )
phone_nok.place(x=2, y=31)

phone_nokEntry=Entry(nok_frame, width=30, borderwidth=3, font=('tahoma',10))
phone_nokEntry.place(x=195, y=31)

#Buttons
registerbtn= Button(button_frame, text='Register', bg='black', fg='cadet blue', font=("#57a1f8", 16, 'bold'),
                    width=10, borderwidth=3, height=1, cursor='hand2', command=register)
registerbtn.place(x=10, y=10)

resetbtn= Button(button_frame, text='Reset', bg='black', fg='cadet blue', font=("#57a1f8", 16, 'bold'),
                    width=10, borderwidth=3, height=1, cursor='hand2', command=reset)
resetbtn.place(x=350, y=10)

uploadbtn= Button(button_frame, text='Upload', bg='black', fg='cadet blue', font=("#57a1f8", 16, 'bold'),
                    width=10, borderwidth=3, height=1, cursor='hand2', command=upload)
uploadbtn.place(x=10, y=65)

printbtn= Button(button_frame, text='Print', bg='black', fg='cadet blue', font=("#57a1f8", 16, 'bold'),
                    width=10, borderwidth=3, height=1, cursor='hand2',
                 command=lambda:print(studentDetailsText.get("1.0", END)))
printbtn.place(x=180, y=45)

exitbtn= Button(button_frame, text='Exit', bg='black', fg='cadet blue', font=("#57a1f8", 16, 'bold'),
                    width=10, borderwidth=3, height=1, cursor='hand2', command=exit)
exitbtn.place(x=350, y=61)

#time section
crnt_time= Label(windows, text="Time", width=15, bg='cadet blue', fg='black', font=('#57a1f8', 20, 'bold'))
crnt_time.place(x=450, y=550)

crnt_date=Label(windows, text=f"{date:%A,%B %d, %Y}", width=20, bg='cadet blue', fg='black',
                font=('#57a1f8', 17, 'bold'))
crnt_date.place(x=450, y=600)

time_update()
windows.mainloop()