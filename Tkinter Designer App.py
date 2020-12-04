#importing required modules

import tkinter as tk
import Tkdesigner as Tkg # my module

#configuring window

root=tk.Tk()
root.title("Tkinter Designer")
root.state("zoomed")
root.config(bg="orange")

	
#Heading

Heading_label=tk.Label(root,text="Tkinter Designer",bg="orange")
Heading_label.place(x=330,y=10)
Heading_label.config(font=("Lucida Fax",30))


#Functions
def Create_Window():
	file=open("Example.py","w")

	title=Title_entry.get()
	size=Size_entry.get()
	Tkg.Create.Window(title,size)
	


def Create_Label():
	
	text=text_entry.get()
	X_axis=X_axis_entry.get()
	Y_axis=Y_axis_entry.get()
	Bg=Bg_entry.get()
	Fg=Fg_entry.get()
	Tkg.Create.Label(text,X_axis,Y_axis,Bg,Fg)
	

def Create_Entry():
	x=X_axis_ent.get()
	y=Y_axis_ent.get()
	Tkg.Create.Entry(x,y)

def save():
	Tkg.Create.finish()
def Create_More():
	import tkinter as tk

	win=tk.Tk()
	win.title("Create More")
	win.config(bg="orange")
	win.geometry("700x400")
	def Create_menu():
		Tkg.Create.menu()

	def create_Menue(event):
	    Create_Menu.config(bg='black',fg='white')
	def create_Menul(event):
	    Create_Menu.config(bg='white',fg='black')

	Create_Menu=tk.Button(win,text="Create Menubar",command=Create_menu,width=15)
	Create_Menu.place(x=400,y=350)
	Create_Menu.bind('<Enter>',create_Menue)
	Create_Menu.bind('<Leave>',create_Menul)
	

	x_axis_entry=tk.Entry(win)
	x_axis_entry.place(x=60,y=100)
	

	
	def create_Buttons():
		
		text_in_Button=text_entry.get()
		x=x_axis_entry.get()
		y=y_axis_entry.get()
		Tkg.Create.Button(text_in_Button,x,y)

	x_axis_label=tk.Label(win,text="Enter The x coordinate",bg="orange")
	x_axis_label.place(x=60,y=50)
	x_axis_label.config(font=("Lucida Fax",20))
	


	y_axis_label=tk.Label(win,text="Enter The y coordinate",bg="orange")
	y_axis_label.place(x=60,y=150)
	y_axis_label.config(font=("Lucida Fax",20))
	y_axis_entry=tk.Entry(win)
	y_axis_entry.place(x=60,y=200)



	text_label=tk.Label(win,text="Enter The Text to appear in Button",bg="orange")
	text_label.place(x=60,y=250)
	text_label.config(font=("Lucida Fax",20))
	text_entry=tk.Entry(win)
	text_entry.place(x=60,y=300)

	def create_Buttone(event):
	    Create_Button.config(bg='black',fg='white')
	def create_Buttonl(event):
	    Create_Button.config(bg='white',fg='black')


	Create_Button=tk.Button(win,text="Create Button",command=create_Buttons,width=15)
	Create_Button.place(x=100,y=350)
	Create_Button.bind('<Enter>',create_Buttone)
	Create_Button.bind('<Leave>',create_Buttonl)
	

	win.mainloop()


def sample1():
	Tkg.Create.HelloWorld()
	Tkg.Create.finish()

def sample2():
	Tkg.Create.HelloWorld_With_Button()
	Tkg.Create.finish()

def sample3():
	Tkg.Create.Print_Entry()
	Tkg.Create.finish()

menubar = tk.Menu(root)#menu bar
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Save code as example.py",command=save)
filemenu.add_command(label="Create More",command=Create_More)


filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Options", menu=filemenu)
Sample=tk.Menu(menubar, tearoff=0)
Sample.add_command(label="Hello world program",command=sample1)
Sample.add_command(label="Hello world program with Button",command=sample2)
Sample.add_command(label="Print Entry",command=sample3)
menubar.add_cascade(label="Sample", menu=Sample)




#Labels and entry
Title_label=tk.Label(root,text="Enter The Title",bg="orange")
Title_label.place(x=60,y=130)
Title_label.config(font=("Lucida Fax",20))
Title_entry=tk.Entry(root)
Title_entry.place(x=60,y=180)

Size_label=tk.Label(root,text="Enter The Size",bg="orange")
Size_label.place(x=60,y=210)
Size_label.config(font=("Lucida Fax",20))
Size_entry=tk.Entry(root)
Size_entry.place(x=60,y=260)

def create_windowe(event):
    Create_Window.config(bg='black',fg='white')
def create_windowl(event):
    Create_Window.config(bg='white',fg='black')

#widgets
Create_Window=tk.Button(root,text="Create Window",command=Create_Window,bg='white')
Create_Window.place(x=60,y=310)
Create_Window.bind('<Enter>',create_windowe)
Create_Window.bind('<Leave>',create_windowl)

text_label=tk.Label(root,text="Enter The Text to be shown in Label",bg="orange")
text_label.place(x=60,y=350)
text_label.config(font=("Lucida Fax",20))
text_entry=tk.Entry(root)
text_entry.place(x=60,y=410)


X_axis_label=tk.Label(root,text="Enter The x coordinate",bg="orange")
X_axis_label.place(x=60,y=450)
X_axis_label.config(font=("Lucida Fax",20))
X_axis_entry=tk.Entry(root)
X_axis_entry.place(x=60,y=500)

Y_axis_label=tk.Label(root,text="Enter The y coordinate",bg="orange")
Y_axis_label.place(x=60,y=550)
Y_axis_label.config(font=("Lucida Fax",20))
Y_axis_entry=tk.Entry(root)
Y_axis_entry.place(x=60,y=600)

Bg_label=tk.Label(root,text="Enter The Bg Colour",bg="orange")
Bg_label.place(x=500,y=450)
Bg_label.config(font=("Lucida Fax",20))
Bg_entry=tk.Entry(root)
Bg_entry.place(x=500,y=500)

Fg_label=tk.Label(root,text="Enter The Fg Colour",bg="orange")
Fg_label.place(x=500,y=550)
Fg_label.config(font=("Lucida Fax",20))
Fg_entry=tk.Entry(root)
Fg_entry.place(x=500,y=600)

def create_labele(event):
    Create_Label.config(bg='black',fg='white')
def create_labell(event):
    Create_Label.config(bg='white',fg='black')

Create_Label=tk.Button(root,text="Create Label",command=Create_Label,width=15)
Create_Label.place(x=350,y=640)
Create_Label.bind('<Enter>',create_labele)
Create_Label.bind('<Leave>',create_labell)

X_axis_lbl=tk.Label(root,text="Enter The X coordinate for entry box",bg="orange")
X_axis_lbl.place(x=500,y=130)
X_axis_lbl.config(font=("Lucida Fax",20))
X_axis_ent=tk.Entry(root)
X_axis_ent.place(x=500,y=180)

Y_axis_lbl=tk.Label(root,text="Enter The Y coordinate for entry box",bg="orange")
Y_axis_lbl.place(x=500,y=210)
Y_axis_lbl.config(font=("Lucida Fax",20))
Y_axis_ent=tk.Entry(root)
Y_axis_ent.place(x=500,y=260)


def create_Entrye(event):
    Create_Entry.config(bg='black',fg='white')
def create_Entryl(event):
    Create_Entry.config(bg='white',fg='black')


Create_Entry=tk.Button(root,text="Create Entry",command=Create_Entry,width=15,bg='white')
Create_Entry.place(x=500,y=300)
Create_Entry.bind('<Enter>',create_Entrye)
Create_Entry.bind('<Leave>',create_Entryl)

root.config(menu=menubar)
root.mainloop()#loop

#detail explanation in Readme file
#Developer contact:sriramvkumar007@gmail.com