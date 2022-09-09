from tkinter import *
from tkinter import messagebox
from db import Database




db = Database("spaced_interval.db")



def days_from_last_revision(db_date):
	from datetime import date

	db_date = db_date

	year = int(db_date[0:4]) 
	month = int(db_date[5:7])
	day = int(db_date[8:10])

	db_date = date(year, month, day)

	days = str(date.today() - db_date)[0]

	return int(days)

 

def populate():
	# deleting the pre-existing data
	topics_for_today.delete(0,END)

	techniques = {1: "Feynamnn Technique", 7: "Solve Questions on the topic", 30: "Feynmann Technique"}


	# updating with new data
	for row in db.fetch():

		days = days_from_last_revision(row[3])

		if days in techniques:
			topics_for_today.insert(END, row[1])
			source.insert(END, row[2])
			technique.insert(END, techniques[days])


	return



def add_topic():
	if topic_text.get() == '' or source_text.get() =='':
		messagebox.showerror('Required Field', 'Please include the Topic and Source')
		return

	from datetime import date
	current_date = date.today()

	db.insert(topic_text.get(), current_date, source_text.get())
	#topics_for_today.delete(0,END)


	print("Topic Added to Database")




##################################################################################################################

# creating window object
app = Tk()

app.title("learning log")
app.geometry("1183x384")


# For entry of todays topic
# Part--> matrix[0][0]
topic_text = StringVar()
topic_label = Label(app, text="Today I Learnt:", font=("bold",10))
topic_label.grid(row=0, column=1) #alligning the part to the west(left) of the text
# Part--> matrix[0][1]
topic_entry = Entry(app, textvariable=topic_text) #for entry of data
topic_entry.grid(row=0, column=2)


# For entry of source of learning(book/course/tutorial etc.)
source_text = StringVar()
source_label = Label(app, text="Source to refer:", font=("bold",10))
source_label.grid(row=0, column=4) #alligning the part to the west(left) of the text
# Part--> matrix[0][1]
source_entry = Entry(app, textvariable=source_text) #for entry of data
source_entry.grid(row=0, column=5)


# Buttons
add_btn  = Button(app, text="Add Topic", width=12, command=add_topic)
add_btn.grid(row=2, column=3, pady=10)



# Topics to be revised today list box
part_labelTopics = Label(app, text="Topics to revise today", font=("bold",10), pady=10)
part_labelTopics.grid(row=3, column=0) #alligning the part to the west(left) of the text
topics_for_today = Listbox(app)
topics_for_today.grid(row=4, column=0, rowspan=6)
# create scroll bar
scrollbar = Scrollbar(app)
scrollbar.grid(row=4, column=1)
# Set scroll to listbox
topics_for_today.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=topics_for_today.yview)




# Sources
part_label_source = Label(app, text="Source(from where to revise)", font=("bold",10), pady=10)
part_label_source.grid(row=3, column=2) #alligning the part to the west(left) of the text
source = Listbox(app)
source.grid(row=4, column=2,rowspan=6)
# create scroll bar
scrollbar = Scrollbar(app)
scrollbar.grid(row=4, column=3)
# Set scroll to listbox
source.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=source.yview)




# Revision Technique
part_label_technique = Label(app, text="Technique(how to revise)", font=("bold",10), pady=10)
part_label_technique.grid(row=3, column=4) #alligning the part to the west(left) of the text
technique = Listbox(app)
technique.grid(row=4, column=4,rowspan=6)
# create scroll bar
scrollbar = Scrollbar(app)
scrollbar.grid(row=4, column=5)
# Set scroll to listbox
technique.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=technique.yview)





# Status
part_labelStatus = Label(app, text="Revision Status", font=("bold",10), pady=10)
part_labelStatus.grid(row=3, column=6, sticky=W) #alligning the part to the west(left) of the text
status = Listbox(app)
status.grid(row=4, column=6,rowspan=6)
# create scroll bar
scrollbar = Scrollbar(app)
scrollbar.grid(row=4, column=7)
# Set scroll to listbox
status.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=status.yview)


# Calling the function to populate the "for today", "resource" and "status" sections.
populate()


# start mainloop
app.mainloop()