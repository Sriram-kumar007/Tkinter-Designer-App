READ ME

WHAT IS IT?

This projects is developed with the motive of helping the beeginers to learn tkinter module and also for experts how are bored of typing each and every line for making a tkinter project,My project make this ease this has a simple gui to help you .You can just enter the coordinates and this project will give you a basic outline of your project as "example.py".In this project I have included my own module namely "Tkdesigner".This project has some simple programs as inbuilt data.

HOW TO RUN?

To run this you have to download my Tkdesigner.py and just run main.py.

CODE EXPLAINATION:


import tkinter as tk - importing tkinter for making window
import Tkdesigner as Tkg - importing Tkdesigner(my module)

root=tk.Tk() - assigning tkinter to root
root.title("Tkinter Designer") - adding title
root.state("zoomed") - adding state
root.config(bg="orange") - adding bg colour

Heading_label=tk.Label(root,text="Tkinter Designer",bg="orange")
Heading_label.place(x=330,y=10)
Heading_label.config(font=("Lucida Fax",30)) - heading


def Create_Window(): - defining function
	file=open("Example.py","w") - asking python to create a file
	title=Title_entry.get() 
	size=Size_entry.get()
	Tkg.Create.Window(title,size)

def Create_Label(): - defining function
	
	text=text_entry.get()     
	X_axis=X_axis_entry.get()
	Y_axis=Y_axis_entry.get()   - assigning variable to entry.get()
	Bg=Bg_entry.get()
	Fg=Fg_entry.get()
	Tkg.Create.Label(text,X_axis,Y_axis,Bg,Fg)  - using Tk designer module to 
												  create label
def Create_Entry(): - defining function
	x=X_axis_ent.get()
	y=Y_axis_ent.get() - assigning variable to entry.get()
	Tkg.Create.Entry(x,y) -  - using Tk designer module to 
							   create Entry box

def save(): - defining function
	Tkg.Create.finish() - using Tk designer module to 
						  save file

def Create_More(): defining a function
	import tkinter as tk

	win=tk.Tk()
	win.title("Create More")
	win.config(bg="orange")  - creating new window  for more options
	win.geometry("700x400")


	def Create_menu(): - defining function
		Tkg.Create.menu() -  using Tk designer module to 
						     create menu bar

	
	

	
	def create_Buttons(): - defining function
		
		text_in_Button=text_entry.get()
		x=x_axis_entry.get()
		y=y_axis_entry.get()  - assigning variables to entry.get(*)
		Tkg.Create.Button(text_in_Button,x,y)  -using Tk designer module to 
						     					create Buttons

	
	win.mainloop()


def sample1(): - defining function
	Tkg.Create.HelloWorld() - using Tk designer module to 
						     create Hello world program

	
	Tkg.Create.finish()

def sample2(): - defining function
	Tkg.Create.HelloWorld_With_Button()- using Tk designer module to 
						     create Hello world eith button program

	Tkg.Create.finish()

def sample3(): - defining function
	Tkg.Create.Print_Entry()- using Tk designer module to 
						     create Print Entry program

	Tkg.Create.finish()


menubar = tk.Menu(root) - creating menu bar
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


In this code explaination i have explained only the important code in this progrom

Advantages:
	
	1.As I mentioned earlier it will be helpful for beginners to learn tkinter

	2.It will be helpful for experts to have a basic outline of tkinter

Disadvantages:

	1.Th file name cannot be changed from gui.It can be only changed from source code

	
Developer contact:sriramvkumar007@gmail.com
