from tkinter import *
import DS_Model_backend

def update1():
    list1.delete(0,END)
    list1.insert(END, "Pain Present = Yes")
    DS_Model_backend.delete1()
    DS_Model_backend.insert1()
def update2():
    list1.delete(0,END)
    list1.insert(END, "Pain Present = No")
    DS_Model_backend.delete2()
    DS_Model_backend.insert2()

def view_command():
    list1.delete(0,END)
    DS_Model_backend.insertDSModel()
    results = DS_Model_backend.view()
    for result in results:
        list1.insert(END, result)
    DS_Model_backend.deleteDSModel()

def delete_command():
    list1.delete(0,END)

def add_model_command():
    list1.delete(0,END)
    list1.insert(END, "Model added")
    DS_Model_backend.clear()
    DS_Model_backend.add_model()

def clear_command():
    list1.delete(0,END)
    DS_Model_backend.clear()


window = Tk()
window.wm_title("DS Model Dentistry")

l1 = Label(window,text="Pain Present")
l1.grid(row=0,column=0)

b1 = Button(window,width=12, text="Yes",command=update1)
b1.grid(row=0,column=1)

b2= Button(window,width=12,text="No",command=update2)
b2.grid(row=0,column=3)


b3 = Button(window,width=12,text="Get Diagnosis", command=view_command)
b3.grid(row=6,column=3)

list1 = Listbox(window,height=8, width=50)
list1.grid(row=5, column=0,rowspan=7, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=5,column=2, rowspan=7)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b4 = Button(window,text="Add Model", width=12,command=add_model_command)
b4.grid(row=5,column=3)

b5 = Button(window,text="Clear data", width=12,command=clear_command)
b5.grid(row=7,column=3)

b5 = Button(window,text="Close", width=12, command=window.destroy)
b5.grid(row=8,column=3)

window.mainloop()

