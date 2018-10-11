from tkinter import *
from backend import Database

database = Database("books.db")

class Window(object):

	def __init__(self, window):

		self.window = window

		self.window.wm_title("Bookstore")

		
		l1 = Label(window, text="Title")
		l1.grid(row=0, column=0)

		self.title_input=StringVar()
		self.e1 = Entry(window, textvariable=self.title_input)
		self.e1.grid(row=0, column=1)

		l2 = Label(window, text="Year")
		l2.grid(row=1, column=0)

		self.year_input=StringVar()
		self.e2 = Entry(window, textvariable=self.year_input)
		self.e2.grid(row=1, column=1)

		l3 = Label(window, text="Author")
		l3.grid(row=0, column=2)

		self.author_input=StringVar()
		self.e3 = Entry(window, textvariable=self.author_input)
		self.e3.grid(row=0, column=3)

		l4 = Label(window, text="ISBN")
		l4.grid(row=1, column=2)

		self.isbn_input=StringVar()
		self.e4 = Entry(window, textvariable=self.isbn_input)
		self.e4.grid(row=1, column=3)

		b1 = Button(window, text="View All", width=12, command=self.view_command)
		b1.grid(row=2, column=3)

		b2 = Button(window, text="Search Entry", width=12, command=self.search_command)
		b2.grid(row=3, column=3)

		b3 = Button(window, text="Add Entry", width=12, command=self.add_command)
		b3.grid(row=4, column=3)

		b4 = Button(window, text="Update", width=12, command=self.update_command)
		b4.grid(row=5, column=3)

		b5 = Button(window, text="Delete", width=12, command=self.delete_command)
		b5.grid(row=6, column=3)

		b6 = Button(window, text="Close", width=12, command=self.window.destroy)
		b6.grid(row=7, column=3)

		self.t1 = Listbox(window, height=6, width=35)
		self.t1.grid(row=2, column=0, rowspan=6, columnspan=2)

		self.t1.bind('<<ListboxSelect>>', self.get_selected_row)

		sb1=Scrollbar(window)
		sb1.grid(row=2, column=2, rowspan=6)

		self.t1.configure(yscrollcommand=sb1.set)
		b1.configure(command=self.t1.yview)

	def view_command(self):
		self.t1.delete(0, END)
		for row in database.view():
			self.t1.insert(END, row)

	def search_command(self):
		self.t1.delete(0, END)
		for row in backend.search(self.title_input.get(), self.author_input.get(), self.year_input.get(), self.isbn_input.get()):
			self.t1.insert(END, row)

	def add_command(self):
		database.insert(self.title_input.get(), self.author_input.get(), self.year_input.get(), self.isbn_input.get())
		self.t1.delete(0, END)
		self.t1.insert(END, (self.title_input.get(), self.author_input.get(), self.year_input.get(), self.isbn_input.get()))

	def get_selected_row(self, event):
		try:
			global selected_row
			index=self.t1.curselection()[0]
			self.selected_row=self.t1.get(index)
			self.e1.delete(0, END)
			self.e1.insert(END, self.selected_row[1])
			self.e2.delete(0, END)
			self.e2.insert(END, self.selected_row[3])
			self.e3.delete(0, END)
			self.e3.insert(END, self.selected_row[2])
			self.e4.delete(0, END)
			self.e4.insert(END, self.selected_row[4])
		except IndexError:
			pass


	def delete_command():
		database.delete(self.selected_row[0])

	def update_command():
		database.update(self.selected_row[0], self.title_input.get(), self.author_input.get(), self.year_input.get(), self.isbn_input.get())




	

window=Tk()
Window(window)
window.mainloop()