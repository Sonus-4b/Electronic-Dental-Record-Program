# dynamic viewport testing
from tkinter import *
from tkinter import ttk

# have save_to_file remove brackets and remove entry sentences if that entry wasnt filled

# doc stuff



def open_consent():
    clear_view()
    global index_num
    index_num = 0
    conLbl.pack()
    default.pack()
    master_accept_button.pack(side=LEFT,expand=TRUE,fill=X)
    delete_button.pack(side=RIGHT,expand=TRUE,fill=X)

def open_scalpel():
    clear_view()
    global index_num
    index_num = 5
    scalpel_lbl.pack()
    scalListbox.pack()
    master_accept_button.pack(side=LEFT, expand=TRUE, fill=X)
    delete_button.pack(side=RIGHT, expand=TRUE, fill=X)

def open_blood():
    clear_view()
    global index_num
    index_num = 1
    bloodLbl.pack()
    default.pack()
    master_accept_button.pack(side=LEFT, expand=TRUE, fill=X)
    delete_button.pack(side=RIGHT, expand=TRUE, fill=X)

def open_heart():
    clear_view()
    global index_num
    index_num = 2
    heartLbl.pack()
    default.pack()
    master_accept_button.pack(side=LEFT, expand=TRUE, fill=X)
    delete_button.pack(side=RIGHT, expand=TRUE, fill=X)

def open_flap():
    clear_view()
    global index_num
    index_num = 6
    flapLbl.pack()
    flapListbox.pack()
    master_accept_button.pack(side=LEFT, expand=TRUE, fill=X)
    delete_button.pack(side=RIGHT, expand=TRUE, fill=X)

def open_anes():
    clear_view()
    global index_num
    index_num = 3
    anesLbl.pack()
    default.pack()
    master_accept_button.pack(side=LEFT, expand=TRUE, fill=X)
    delete_button.pack(side=RIGHT, expand=TRUE, fill=X)

def open_ext():
    clear_view()
    global index_num
    index_num = 4
    extLbl.pack()
    extListbox.pack()
    master_accept_button.pack(side=LEFT, expand=TRUE, fill=X)
    delete_button.pack(side=RIGHT, expand=TRUE, fill=X)

def open_elevator():
    clear_view()
    global index_num
    index_num = 7
    elvLbl.pack()
    default.pack()
    master_accept_button.pack(side=LEFT, expand=TRUE, fill=X)
    delete_button.pack(side=RIGHT, expand=TRUE, fill=X)

def open_removal():
    clear_view()
    global index_num
    index_num = 9
    remLbl.pack()
    remListbox.pack()
    master_accept_button.pack(side=LEFT, expand=TRUE, fill=X)
    delete_button.pack(side=RIGHT, expand=TRUE, fill=X)

def open_hand():
    clear_view()
    global index_num
    index_num = 8
    handLbl.pack()
    handListbox.pack()
    master_accept_button.pack(side=LEFT,expand=TRUE,fill=X)
    delete_button.pack(side=RIGHT,expand=TRUE,fill=X)

def open_irrigation():
    clear_view()
    global index_num
    index_num = 10
    irrLbl.pack()
    irrListbox.pack()
    master_accept_button.pack(side=LEFT, expand=TRUE, fill=X)
    delete_button.pack(side=RIGHT, expand=TRUE, fill=X)

def open_packing():
    clear_view()
    global index_num
    index_num = 11
    pacLbl.pack()
    default.pack()
    master_accept_button.pack(side=LEFT, expand=TRUE, fill=X)
    delete_button.pack(side=RIGHT, expand=TRUE, fill=X)

def open_suture():
    clear_view()
    global index_num
    index_num = 12
    sutureLbl.pack()
    sutureListbox.pack()
    master_accept_button.pack(side=LEFT, expand=TRUE, fill=X)
    delete_button.pack(side=RIGHT, expand=TRUE, fill=X)

def open_provider():
    clear_view()
    global index_num
    index_num = 13
    provLbl.pack()
    default.pack()
    master_accept_button.pack(side=LEFT, expand=TRUE, fill=X)
    delete_button.pack(side=RIGHT, expand=TRUE, fill=X)

# clears the view port
def clear_view():
    for widget in viewField.winfo_children():
        widget.pack_forget()

def open_master(index):
    func_field_index[index]()


def gen_entries():
    counter = 0
    x_pos = 10
    y_pos = 10
    for ent in range(len(entryButtons)):
        entryButtons[counter].place(x=x_pos,y=y_pos)
        entryFields[counter].place(x=90,y=y_pos)
        counter = counter + 1
        y_pos = y_pos + 30

def add_items(items,myListbox):
    counter = 0
    for i in range(len(items)):
        myListbox.insert(END, items[counter])
        counter = counter + 1

def save_to_file(event=None):
    conLine = f'Consent {conValues}. '
    bloodLine = f'Blood Pressure - {bloodValues}. '
    heartLine = f'Heart Rate - {heartValues}. '
    anesLine = f'Anesthetic - {anesValues}. '
    extLine = f'Extraction Type - {extValues}.'
    scalpelLine = f'\nMade incision with {scalpelValues}'
    flapLine = f'scalpel for {flapValues}.'
    elevLine = f'\n{elvValues} luxated tooth with elevator. '
    handLine = f'Used surgical handpiece to {handValues} section tooth, remove bone with copious irrigation.'
    remLine = f'\n{remValues}. '
    irrLine = f'Irrigation - {irrValues}. '
    packLine = f'Packing - {pacValues}. '
    sutLine = f'Sutures - {sutureValues}.'
    provLine = f'\nSurgical procedures by {provValues}.'
    bad_chars = ['[', ']', "'"]

    edr_list = [conLine,bloodLine,heartLine,anesLine,extLine,scalpelLine,flapLine,elevLine,handLine,remLine,irrLine,packLine,sutLine,provLine]
    chosen_list = []
    counter = 0
    # loop to remove lines with empty entries
    for i in range(len(edr_list)):
        if len(values_index[counter]) == 0:
            print('empty')
        elif values_index[counter] == ['']:
            print('empty')
        elif values_index[counter] == [[]]:
            print('empty')
        else:
            chosen_list.append(edr_list[counter])
        counter = counter + 1
    # unwanted characters filter
    newFile = open("EDR-EXT.txt", "w")
    newFile.writelines(chosen_list)
    newFile.close()
    newFile = open("EDR-EXT.txt", 'r')
    final_doc = newFile.read()
    final_doc = ''.join(i for i in final_doc if not i in bad_chars)
    newFile.close()
    newFile = open("EDR-EXT.txt", 'w')
    newFile.write(final_doc)
    newFile.close()
    print('File saved')

root = Tk()
menu = Menu(root)
root.config(menu=menu)

# cascade menu
file = Menu(menu,tearoff=0)
file.add_command(label='Extraction')
menu.add_cascade(label='File',menu=file)

edit = Menu(menu,tearoff=0)
edit.add_command(label='Save ctrl+s',command=save_to_file)
menu.add_cascade(label='Edit',menu=edit)

viewField = LabelFrame(root,text="viewport",height=200,width=170)
viewField.place(x=275,y=10)




# main entry and button objects
_consent = Button(text="Consent",command=open_consent,width=10)
_scalpel = Button(text='Scalpel',command=open_scalpel,width=10)
_blood_pressure = Button(text='Blood Pres.',command=open_blood,width=10)
_heart_rate = Button(text='Heart Rate',command=open_heart,width=10)
_anes = Button(text='Anesthetic',command=open_anes,width=10)
_ext_type = Button(text='Ext. Type',width=10,command=open_ext)
_flap = Button(text='Flap',width=10,command=open_flap)
_elevator = Button(text='Elevator',command=open_elevator,width=10)
_handpiece = Button(text='Hand Piece',command=open_hand,width=10)
_removal = Button(text='Removal',command=open_removal,width=10)
_irrigation = Button(text='Irrigation',command=open_irrigation,width=10)
_packing = Button(text='Packing',command=open_packing,width=10)
_sutures = Button(text='Sutures',width=10,command=open_suture)
_provider = Button(text='Provider',command=open_provider,width=10)

conEnt = Entry()
conLbl = Label(viewField,text='Consent')
conValues = []
scalEnt = Entry()
bloodEnt = Entry()
bloodLbl = Label(viewField,text='Blood Pressure')
bloodValues = []
heartEnt = Entry()
heartLbl = Label(viewField,text='Heart Rate')
heartValues = []
anesEnt = Entry()
anesLbl = Label(viewField,text='Anesthetic')
anesValues = []
extEnt = Entry()
flapEnt = Entry()
elvEnt = Entry()
elvLbl = Label(viewField,text='Elevator')
elvValues = []
handEnt = Entry()
remEnt = Entry()
irrEnt = Entry()
pacEnt = Entry()
pacLbl = Label(viewField,text='Packing')
pacValues = []
sutEnt = Entry()
provEnt = Entry()
provLbl = Label(viewField,text='Provider')
provValues = []



saveButton = Button(text='OK', width=6,command=save_to_file)
saveButton.place(x=275,y=310)

entryButtons = [_consent,_blood_pressure,_heart_rate,_anes,_ext_type,_scalpel,_flap,_elevator,_handpiece,_removal,_irrigation,_packing,_sutures,_provider]
entryFields = [conEnt,bloodEnt,heartEnt,anesEnt,extEnt,scalEnt,flapEnt,elvEnt,handEnt,remEnt,irrEnt,pacEnt,sutEnt,provEnt]
gen_entries()

default = Listbox(viewField,height=12,width=30)
default.pack()


# Scalpel view
scalListbox = Listbox(viewField,selectmode='multiple',width=30,height=12)
scalItems = ['Size 11','Size 12','Size 15']
scalpel_lbl = Label(viewField,text='Scalpel Size')
add_items(scalItems,scalListbox)
scalpelValues = []



# Ext view
extLbl = Label(viewField,text='Ext. type')
extListbox = Listbox(viewField,selectmode="multiple",width=30,height=12)
extItems = ['coronal remnants deciduous','full bony impaction','impacted root removal','partial bony impaction','surgical','soft tissue impaction','simple']
add_items(extItems,extListbox)
extValues = []


def master_accept(event=None):
    global index_num
    print(menu_index[index_num].winfo_class())
    if menu_index[index_num].winfo_class() == 'Listbox':
        selected_text_list = [menu_index[index_num].get(i) for i in menu_index[index_num].curselection()]
        values_index[index_num].append(selected_text_list)
        print(values_index[index_num])
        #print(len(values_index[index_num]))
    else:
        single_text = menu_index[index_num].get()
        values_index[index_num].append(single_text)
        print(values_index[index_num])
        #print(len(values_index[index_num]))

    index_num = index_num + 1
    print(index_num)
    if index_num == len(menu_index):
        index_num = 0
    open_master(index_num)

def delete_last_entry():
    global index_num
    values_index[index_num].pop()
    print(values_index[index_num])




master_accept_button = Button(viewField,text='Accept',command=master_accept)
root.bind('<Control_L>',master_accept)
root.bind('<Control-s>',save_to_file)
delete_button = Button(viewField,text='Delete',command=delete_last_entry)



# flap view
flapLbl = Label(viewField,text='Flap')
flapListbox = Listbox(viewField,selectmode='multiple',width=30,height=12)
flapItems = ['Buccal flap','Envelope flap','release incn']
add_items(flapItems,flapListbox)
flapValues = []


# hand view
handLbl = Label(viewField,text='Hand Piece')
handListbox = Listbox(viewField,selectmode='multiple',width=30,height=12)
handItems = ['Section tooth','Remove bone']
add_items(handItems,handListbox)
handValues = []


# rem view
remLbl = Label(viewField,text='Removal')
remListbox = Listbox(viewField,selectmode='multiple',width=30,height=12)
remItems = ['Extracted tooth with forceps','Elevated roots separately']
add_items(remItems,remListbox)
remValues = []

# irrigation view
irrLbl = Label(viewField,text='Irrigation')
irrListbox = Listbox(viewField,selectmode='multiple',width=30,height=12)
irrItems = ['0.12% chlorhexidine gluconate','0.9% sodium chloride']
add_items(irrItems,irrListbox)
irrValues = []

# suture view
sutureLbl = Label(viewField,text='Sutures')
sutureListbox = Listbox(viewField,selectmode='multiple',width=30,height=12)
sutureItems = ['one gut suture','two gut sutures','three gut sutures','four gut sutures','one silk suture','two silk sutures','three silk sutures','four silk sutures']
add_items(sutureItems,sutureListbox)
sutureValues = []


index_num = 0
menu_index = [conEnt,bloodEnt,heartEnt,anesEnt,extListbox,scalListbox,flapListbox,elvEnt,handListbox,remListbox,irrListbox,pacEnt,sutureListbox,provEnt]
values_index = [conValues,bloodValues,heartValues,anesValues,extValues,scalpelValues,flapValues,elvValues,handValues,remValues,irrValues,pacValues,sutureValues,provValues]
func_field_index = [open_consent,open_blood,open_heart,open_anes,open_ext,open_scalpel,open_flap,open_elevator,open_hand,open_removal,open_irrigation,open_packing,open_suture,open_provider]


root.geometry('500x500')
root.mainloop()
