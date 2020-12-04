from tkinter import*

root=Tk()
root.title("preview")

class Create(object):

	global file
	file=open("Example.py","w")

	
	file.write("from tkinter import* \n")
	file.write("root=Tk() \n")
	

	def Window(title,size):
		
		
		
		root.title(title)
		root.geometry(size)
		
		file.write(f"root.title(\'{title}\')\n")

		file.write(f"root.geometry(\'{size}\')\n")

	def Label(text,x,y,bg,fg):
		

		label=Label(root,text=text,bg=bg,fg=fg)
		label.place(x=int(x),y=int(y))
		
		


		file.write(f"label=Label(root,text=\'{text}\',bg=\'{bg}\',fg=\'{fg}\')\n")
		file.write(f"label.place(x={int(x)},y={int(y)})\n")
		
	
	def Entry(x,y):

		entry=Entry(root)
		entry.place(x=int(x),y=int(y))



		file.write(f"entry=Entry(root)\n")
		file.write(f"entry.place(x={int(x)},y={int(y)})\n")
		file.write(f"TextInEntry=entry.get()\n")
	

		

		
	def Button(text,x,y):
		
		button=Button(root,text=text)
		button.place(x=int(x),y=int(y))

		file.write(f"button=Button(root,text=\'{text}\',command=NONE)\n")
		file.write(f"button.place(x={int(x)},y={int(y)})\n")
	

	def menu():

		menubar = Menu(root)
		filemenu = Menu(menubar, tearoff=0)
		filemenu.add_command(label="New")
		filemenu.add_command(label="Open")
		filemenu.add_command(label="Save")
		filemenu.add_command(label="Save as...")
		filemenu.add_command(label="Close")

		filemenu.add_command(label="Exit", command=root.quit)
		menubar.add_cascade(label="File", menu=filemenu)
		editmenu = Menu(menubar, tearoff=0)
		editmenu.add_command(label="Undo")

		editmenu.add_separator()

		editmenu.add_command(label="Cut")
		editmenu.add_command(label="Copy")
		editmenu.add_command(label="Paste")
		editmenu.add_command(label="Delete")
		editmenu.add_command(label="Select All")
		menubar.add_cascade(label="Edit", menu=editmenu)

		root.config(menu=menubar)



		file.write(f"menubar = Menu(root)\n")
		file.write(f"filemenu = Menu(menubar, tearoff=0)\n")
		file.write(f"filemenu.add_command(label='New')\n")
		file.write(f"filemenu.add_command(label='Open')\n")
		file.write(f"filemenu.add_command(label='Save')\n")
		file.write(f"filemenu.add_command(label='Save as...')\n")
		file.write(f"filemenu.add_command(label='Close')\n")
		file.write(f"filemenu.add_command(label='Exit', command=root.quit)\n")
		file.write(f"menubar.add_cascade(label='File', menu=filemenu)\n")
		file.write(f"editmenu = Menu(menubar, tearoff=0)\n")

		file.write(f"editmenu.add_command(label='Undo')\n")
		file.write(f"editmenu.add_separator()\n")
		file.write(f"editmenu.add_command(label='Cut')\n")
		file.write(f"editmenu.add_command(label='Copy')\n")
		file.write(f"editmenu.add_command(label='Paste')\n")
		file.write(f"editmenu.add_command(label='Delete')\n")
		file.write(f"editmenu.add_command(label='Select All')\n")
		file.write(f"menubar.add_cascade(label='Edit', menu=editmenu)\n")
		file.write(f"root.config(menu=menubar)\n")





	def HelloWorld():
		root.title("Sample")
		label=Label(root,text="Helloworld",bg="yellow",fg="black")
		label.place(x=50,y=50)

		file.write(f"root.title('Sample')\n")

		file.write(f"label=Label(root,text='Hello world',bg='Yellow',fg='Black')\n")
		file.write(f"label.pack()\n")

	def HelloWorld_With_Button():
		root.title("Sample")

		def function():
			label=Label(root,text="Helloworld",bg="yellow",fg="black")
			label.pack()

		button=Button(root,text="Click Me",command=function)
		button.place(x=50,y=50)

		file.write(f"root.title('Sample')\n")
		file.write(f"def function():\n")
		file.write(f"\tlabel=Label(root,text='Helloworld',bg='yellow',fg='black')\n")
		file.write(f"\tlabel.pack()\n")
		file.write(f"button=Button(root,text='Click Me',command=function)\n")
		file.write(f"button.place(x=50,y=50)\n")




	def Print_Entry():
		root.title("Sample")
		def function():
			label=Label(root,text=entry.get())
			label.pack()
			print(entry.get())
		entry=Entry(root)
		entry.place(x=50,y=50)
		button=Button(root,text="Click Me",command=function)
		button.place(x=50,y=90)

		file.write(f"root.title('Sample')\n")
		file.write(f"root.title('Sample')\n")
		file.write(f"def function():\n")
		file.write(f"\tlabel=Label(root,text=entry.get())\n")
		file.write(f"\tlabel.pack()\n")
		file.write(f"\tprint(entry.get())\n")
		file.write(f"entry=Entry(root)\n")
		file.write(f"entry.place(x=50,y=50)\n")
		file.write(f"button=Button(root,text='Click Me',command=function)\n")
		file.write(f"button.place(x=50,y=90)\n")



	def finish():


		file.write("root.mainloop() \n")
		root.mainloop()
		file.close()
