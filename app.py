from tkinter import *

def add_topic():
	print("Topic Added")



# creating window object
app = Tk()

app.title("learning log")
app.geometry("700x350")


# Part--> matrix[0][0]
part_text = StringVar()
part_label = Label(app, text="Today I Learnt", font=("bold",14), pady=20)
part_label.grid(row=0, column=0, sticky=W) #alligning the part to the west(left) of the text

# Part--> matrix[0][1]
part_entry = Entry(app, textvariable=part_text) #for entry of data
part_entry.grid(row=0, column=1)


# Topics to be revised today list box
for_today = Listbox(app, height=8, width=50, border=0)
for_today.grid(row=3, column=0, columnspan=3,rowspan=6, pady=20, padx=20)
# create scroll bar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)
# Set scroll to listbox
for_today.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=for_today.yview)

# Buttons
add_btn  = Button(app, text="Add Topic", width=12, command=add_topic)
add_btn.grid(row=2, column=1, pady=20)


# Resources
resource = Listbox(app, height=8, width=50, border=0)
resource.grid(row=3, column=4, columnspan=3,rowspan=6, pady=20, padx=20)



# start mainloop
app.mainloop()