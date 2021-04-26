from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import docx
from datetime import datetime


SCRIPT_NAME = 'anesthesia'
CURRENT_DATE = datetime.today().strftime('%Y-%m-%d')
FILE_NAME = SCRIPT_NAME + "-" + CURRENT_DATE
doc = docx.Document()


def clear_view():
    for widget in viewField.winfo_children():
        widget.pack_forget()
    


def open_master(index):
    func_field_index[index]()


def place_buttons():
    counter = 0
    x_pos = 10
    y_pos = 30
    for ent in range(len(entryButtons)):
        entryButtons[counter].place(x=x_pos,y=y_pos)
        counter = counter + 1
        y_pos = y_pos + 30
    


def add_items(items,myListbox):
    counter = 0
    for i in range(len(items)):
        myListbox.insert(END, items[counter])
        counter = counter + 1



def open_topical():
    clear_view()
    global index_num
    index_num = 0
    topical_lbl.pack()
    topical_listbox.pack()
    master_accept_button.pack(side=LEFT, expand=TRUE, fill=X)
    delete_button.pack(side=RIGHT, expand=TRUE, fill=X)
    topical_listbox.bind('<Double-1>', master_accept)
    


def open_carpule():
    clear_view()
    global index_num
    index_num = 1
    carpule_lbl.pack()
    carpule_listbox.pack()
    master_accept_button.pack(side=LEFT, expand=TRUE, fill=X)
    delete_button.pack(side=RIGHT, expand=TRUE, fill=X)
    carpule_listbox.bind('<Double-1>', master_accept)
    


def open_type():
    clear_view()
    global index_num
    index_num = 2
    type_lbl.pack()
    type_listbox.pack()
    master_accept_button.pack(side=LEFT, expand=TRUE, fill=X)
    delete_button.pack(side=RIGHT, expand=TRUE, fill=X)
    type_listbox.bind('<Double-1>', master_accept)
    


def open_injection():
    clear_view()
    global index_num
    index_num = 3
    injection_lbl.pack()
    injection_listbox.pack()
    master_accept_button.pack(side=LEFT, expand=TRUE, fill=X)
    delete_button.pack(side=RIGHT, expand=TRUE, fill=X)
    injection_listbox.bind('<Double-1>', master_accept)
    


def open_aspiration():
    clear_view()
    global index_num
    index_num = 4
    aspiration_lbl.pack()
    aspiration_listbox.pack()
    master_accept_button.pack(side=LEFT, expand=TRUE, fill=X)
    delete_button.pack(side=RIGHT, expand=TRUE, fill=X)
    aspiration_listbox.bind('<Double-1>', master_accept)
    


def open_carpule_b():
    clear_view()
    global index_num
    index_num = 5
    carpule_b_lbl.pack()
    carpule_b_listbox.pack()
    master_accept_button.pack(side=LEFT, expand=TRUE, fill=X)
    delete_button.pack(side=RIGHT, expand=TRUE, fill=X)
    carpule_b_listbox.bind('<Double-1>', master_accept)
    


def open_type_b():
    clear_view()
    global index_num
    index_num = 6
    type_b_lbl.pack()
    type_b_listbox.pack()
    master_accept_button.pack(side=LEFT, expand=TRUE, fill=X)
    delete_button.pack(side=RIGHT, expand=TRUE, fill=X)
    type_b_listbox.bind('<Double-1>', master_accept)
    


def open_carpule_c():
    clear_view()
    global index_num
    index_num = 7
    carpule_c_lbl.pack()
    carpule_c_listbox.pack()
    master_accept_button.pack(side=LEFT, expand=TRUE, fill=X)
    delete_button.pack(side=RIGHT, expand=TRUE, fill=X)
    carpule_c_listbox.bind('<Double-1>', master_accept)
    


def open_type_c():
    clear_view()
    global index_num
    index_num = 8
    type_c_lbl.pack()
    type_c_listbox.pack()
    master_accept_button.pack(side=LEFT, expand=TRUE, fill=X)
    delete_button.pack(side=RIGHT, expand=TRUE, fill=X)
    type_c_listbox.bind('<Double-1>', master_accept)
    


def open_provider():
    clear_view()
    global index_num
    index_num = 9
    provider_lbl.pack()
    provider_listbox.pack()
    master_accept_button.pack(side=LEFT, expand=TRUE, fill=X)
    delete_button.pack(side=RIGHT, expand=TRUE, fill=X)
    provider_listbox.bind('<Double-1>', master_accept)
    


def save_to_file(event=None):
    #filename = fd.asksaveasfilename(initialdir="/", title="Select a File", filetypes=(("Docx files", "*.docx*"), ("Text files", "*.txt*"),("all files", "*.*")))


    final_doc = text_box.get(1.0, END)
    doc.add_paragraph(final_doc)
    doc.save(f"C:/EDR-scripts/test_docs/{FILE_NAME}.docx")
    print('File saved')


root = Tk()
menu = Menu(root)
root.config(menu=menu)
file = Menu(menu,tearoff=0)
file.add_command(label='Extraction')
menu.add_cascade(label='File',menu=file)
edit = Menu(menu,tearoff=0)
edit.add_command(label='Save ctrl+s',command=save_to_file)
menu.add_cascade(label='Edit',menu=edit)
viewField = LabelFrame(root,text='Insert Note',height=200,width=170)
viewField.place(x=105,y=10)

# text editor
editor_frame = Frame(height=100,width=100, relief=RAISED, borderwidth=1)
editor_frame.place(x=300,y=280)
text_scroll = Scrollbar(editor_frame)
text_scroll.pack(side=RIGHT,fill=Y)
text_box = Text(editor_frame,height=10,width=45,font=('Helvetica',11),undo=True,selectbackground='blue',selectforeground='white',yscrollcommand=text_scroll.set,wrap=WORD)
text_box.pack()
text_scroll.config(command=text_box.yview)


topical_button = Button(text='Topical',command=open_topical,width=10)
topical_listbox = Listbox(viewField,selectmode='multiple',width=30,height=12)
topical_items = ['20% Benzocaine', 'Lidocaine 5%', 'Oraqix Lidocaine 2.5% Prilocaine']
topical_entry = Entry()
topical_lbl = Label(viewField,text='Topical')
add_items(topical_items,topical_listbox)
topical_values = []
topical_paras = {'20% Benzocaine': 'Topical - 20% Benzocaine.','Lidocaine 5%': 'Topical - Lidocaine 5%.', 'Oraqix Lidocaine 2.5% Prilocaine':'Topical - Oraqix Lidocaine 2.5% Prilocaine.'}


carpule_button = Button(text='Carpule(s)',command=open_carpule,width=10)
carpule_listbox = Listbox(viewField,selectmode='multiple',width=30,height=12)
carpule_items = ['1', '2', '3', '4', '5', '6', '7', '8', '.25', '.50', '.75']
carpule_entry = Entry()
carpule_lbl = Label(viewField,text='Carpule(s)')
add_items(carpule_items,carpule_listbox)
carpule_values = []
carpule_paras = {'1': ' 1 carpule(s)','2': ' 2 carpule(s)', '3': ' 3 carpule(s)','4': ' 4 carpule(s)', '5': ' 5 carpule(s)', '6': ' 6 carpule(s)','7': ' 7 carpule(s)',' 8': ' 8 carpule(s)','.25': ' .25 carpule(s)','.50': ' .50 carpule(s)','.75': ' .75 carpule(s)'}

type_button = Button(text='Type',command=open_type,width=10)
type_listbox = Listbox(viewField,selectmode='multiple',width=30,height=12)
type_items = ['4% septocaine', '2% lidocaine', '3% carbocaine plain', '0.5% marcaine HCI', '4% Citanest plain']
type_entry = Entry()
type_lbl = Label(viewField,text='Type')
add_items(type_items,type_listbox)
type_values = []
type_paras = {'4% septocaine': ' of 4% septocaine 1:100,000 epineohrine, 34 mg lido with 17 mcg epi per carpule was delivered','2% lidocaine': ' of 2% lidcaine 1:100,000 epineohrine, 34 mg lido with 17 mcg epi per carpule was delivered','3% carbocaine plain': ' of 3% carbocaine plain 1:100,000 epineohrine was dilivered, 34 mg lido with 17 mcg epi per carpule was delivered','0.5% marcaine HCI': ' of 0.5% marcaine 1:100,000 epineohrine, 34 mg lido with 17 mcg epi per carpule was delivered','4% Citanest plain': ' of 4% cintanest plain 1:100,000 epineohrine, 34 mg lido with 17 mcg epi per carpule was delivered'}

injection_button = Button(text='Injection',command=open_injection,width=10)
injection_listbox = Listbox(viewField,selectmode='multiple',width=30,height=12)
injection_items = ['Infiltration', 'ASA block', 'MSA block', 'PSA block', 'IA block', 'long buccal block', 'ASMA block', 'NP block', 'GP block', 'Gow-Gates block']
injection_entry = Entry()
injection_lbl = Label(viewField,text='injection')
add_items(injection_items,injection_listbox)
injection_values = []
injection_paras = {'Infiltration': ' by infiltration.', 'ASA block': ' by ASA block.','MSA block': ' by MSA block.','PSA block': ' by PSA block.','IA block': ' by IA block.','long buccal block': ' by long buccal block.','ASMA block': 'by ASMA block.','NP block': 'by np block.','GP block': 'by GB block.','Gow-gates block': 'by Gow-gates block.'}

aspiration_button = Button(text='Aspiration',command=open_aspiration,width=10)
aspiration_listbox = Listbox(viewField,selectmode='multiple',width=30,height=12)
aspiration_items = ['no adverse rxn', 'negative aspiration', 'positive aspiration']
aspiration_entry = Entry()
aspiration_lbl = Label(viewField,text='aspiration')
add_items(aspiration_items,aspiration_listbox)
aspiration_values = []
aspiration_paras = {'no adverse rxn': ' no adverse run.','negative aspiration': ' negative aspiration.','positive aspiration': ' positive aspiration.'}

carpule_b_button = Button(text='Carpule(s)',command=open_carpule_b,width=10)
carpule_b_listbox = Listbox(viewField,selectmode='multiple',width=30,height=12)
carpule_b_items = ['1', '2', '3', '4', '5', '6', '7', '8', '.25', '.50']
carpule_b_entry = Entry()
carpule_b_lbl = Label(viewField,text='Carpule(s)')
add_items(carpule_b_items,carpule_b_listbox)
carpule_b_values = []
carpule_b_paras = {'1': ' 1 carpule(s)','2': ' 2 carpule(s)', '3': ' 3 carpule(s)','4': ' 4 carpule(s)', '5': ' 5 carpule(s)', '6': ' 6 carpule(s)','7': ' 7 carpule(s)','8': ' 8 carpule(s)','.25': ' .25 carpule(s)','.50': ' .50 carpule(s)','.75': ' .75 carpule(s)'}

type_b_button = Button(text='Type',command=open_type_b,width=10)
type_b_listbox = Listbox(viewField,selectmode='multiple',width=30,height=12)
type_b_items = ['4% septocaine', '2% lidocaine', '0.5% HCI', '4% Citanest plain']
type_b_entry = Entry()
type_b_lbl = Label(viewField,text='Type')
add_items(type_b_items,type_b_listbox)
type_b_values = []
type_b_paras = {'4% septocaine': ' of 4% septocaine 1:100,000 epineohrine, 34 mg lido with 17 mcg epi per carpule was delivered','2% lidocaine': ' of 2% lidcaine 1:100,000 epineohrine, 34 mg lido with 17 mcg epi per carpule was delivered','3% carbocaine plain': ' of 3% carbocaine plain 1:100,000 epineohrine was dilivered, 34 mg lido with 17 mcg epi per carpule was delivered','0.5% marcaine HCI': ' of 0.5% marcaine 1:100,000 epineohrine, 34 mg lido with 17 mcg epi per carpule was delivered','4% Citanest plain': ' of 4% cintanest plain 1:100,000 epineohrine, 34 mg lido with 17 mcg epi per carpule was delivered'}

carpule_c_button = Button(text='Carpule(s)',command=open_carpule_c,width=10)
carpule_c_listbox = Listbox(viewField,selectmode='multiple',width=30,height=12)
carpule_c_items = ['1', '2', '3', '4', '5', '6', '7', '8', '.25', '.50']
carpule_c_entry = Entry()
carpule_c_lbl = Label(viewField,text='Carpule(s)')
add_items(carpule_c_items,carpule_c_listbox)
carpule_c_values = []
carpule_c_paras = {'1': ' 1 carpule(s)','2': ' 2 carpule(s)', '3': ' 3 carpule(s)','4': ' 4 carpule(s)', '5': ' 5 carpule(s)', '6': ' 6 carpule(s)','7': ' 7 carpule(s)','8': ' 8 carpule(s)','.25': ' .25 carpule(s)','.50': ' .50 carpule(s)','.75': ' .75 carpule(s)'}

type_c_button = Button(text='Type',command=open_type_c,width=10)
type_c_listbox = Listbox(viewField,selectmode='multiple',width=30,height=12)
type_c_items = ['4% septocaine', '3% carbocaine', '2% lidocaine', '0.5% marcaine HCI', '4% Citanist Plain']
type_c_entry = Entry()
type_c_lbl = Label(viewField,text='Type')
add_items(type_c_items,type_c_listbox)
type_c_values = []
type_c_paras = {'4% septocaine': ' of 4% septocaine 1:100,000 epineohrine, 34 mg lido with 17 mcg epi per carpule was delivered','2% lidocaine': ' of 2% lidcaine 1:100,000 epineohrine, 34 mg lido with 17 mcg epi per carpule was delivered','3% carbocaine plain': ' of 3% carbocaine plain 1:100,000 epineohrine was dilivered, 34 mg lido with 17 mcg epi per carpule was delivered','0.5% marcaine HCI': ' of 0.5% marcaine 1:100,000 epineohrine, 34 mg lido with 17 mcg epi per carpule was delivered','4% Citanest Plain': ' of 4% cintanest plain 1:100,000 epineohrine, 34 mg lido with 17 mcg epi per carpule was delivered'}

provider_button = Button(text='Provider',command=open_provider,width=10)
provider_listbox = Listbox(viewField,selectmode='multiple',width=30,height=12)
provider_items = ['Dr. Dug', 'Dr. Smith', 'Dr. MD']
provider_entry = Entry()
provider_lbl = Label(viewField,text='Provider')
add_items(provider_items,provider_listbox)
provider_values = []
provider_paras = {'Dr. Dug': ' Anesthetic delivered by Dr. Dug','Dr. Smith': ' Anesthetic delivered by Dr. Smith','Dr. MD': ' Anesthetic delivered by Dr. MD'}

entryButtons = [topical_button,carpule_button,type_button,injection_button,aspiration_button,carpule_b_button,type_b_button,carpule_c_button,type_c_button,provider_button]
entryFields = [topical_entry,carpule_entry,type_entry,injection_entry,aspiration_entry,carpule_b_entry,type_b_entry,carpule_c_entry,type_c_entry,provider_entry]
menu_index = [topical_listbox,carpule_listbox,type_listbox,injection_listbox,aspiration_listbox,carpule_b_listbox,type_b_listbox,carpule_c_listbox,type_c_listbox,provider_listbox]
values_index = [topical_values,carpule_values,type_values,injection_values,aspiration_values,carpule_b_values,type_b_values,carpule_c_values,type_c_values,provider_values]
paras_index = [topical_paras,carpule_paras,type_paras,injection_paras,aspiration_paras,carpule_b_paras,type_b_paras,carpule_c_paras,type_c_paras,provider_paras]
func_field_index = [open_topical,open_carpule,open_type,open_injection,open_aspiration,open_carpule_b,open_type_b,open_carpule_c,open_type_c,open_provider]


def master_accept(event=None):
    global index_num
    print(menu_index[index_num].winfo_class())
    if menu_index[index_num].winfo_class() == 'Listbox':
        selected_text_list = [menu_index[index_num].get(i) for i in menu_index[index_num].curselection()]
        values_index[index_num].append(selected_text_list)
        text_box.insert(END, paras_index[index_num].get(selected_text_list[0]))
        print(values_index[index_num])
    index_num = index_num + 1
    print(index_num)
    if index_num >= len(menu_index):
        index_num = 0
        print(index_num)
    open_master(index_num)

def delete_last_entry():
    global index_num
    values_index[index_num].pop()
    print(values_index[index_num])

saveButton = Button(text='OK', width=6,command=save_to_file)
saveButton.place(x=580, y=565)
default = Listbox(viewField,height=12,width=30)
default.pack()
place_buttons()
master_accept_button = Button(viewField,text='Accept',command=master_accept)
root.bind('<Control_L>',master_accept)
root.bind('<Control-s>',save_to_file)
delete_button = Button(viewField,text='Delete',command=delete_last_entry)


index_num = 0
open_master(index_num)
root.geometry('700x600')
root.mainloop()
