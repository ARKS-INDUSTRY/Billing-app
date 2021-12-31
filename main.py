from tkinter import *
from random import randint
from pprint import pprint

root = Tk()
root.title("Billing App")
root.geometry("350x1080")
root.iconbitmap("Resources/logo.ico")


def add_item_to_dict():
   global item_price_list
   items = []
   item_list = listbox.curselection()
   for i in item_list:
       item_name = listbox.get(i)
   no_of_item_purchased = default.get()
   for j in range(length):
      if item_name == product_list[j]:
         price_index = j
   item_price = item_price_list[price_index]
   items.append(
       {"item name": item_name, "no_of_items": no_of_item_purchased, "price": item_price})
   pprint(items)
   return items


def bill_amount():
   pass

head_label = Label(root, text="Billing App", font=("aharoni", 30))
head_label.pack(pady=10)
entry_label = Label(root, text="Enter The product name :  ", font=("aharoni", 15))
entry_label.pack(pady=5)

list_entry = Entry(root, width=35, font=("aharoni", 15))
list_entry.pack(pady=5)
no_idea = Label(root, text='''No idea on what you buyed ?
here is the list that we have in our shop :)''', font=("aharoni", 15))
no_idea.pack(pady=15)
frame = Frame(root, height=45)
listbox = Listbox(frame, width=35, height=15, font=("aharoni", 15))
product_list = ["Bananas", "Water", "Milk", "Beef", "Eggs", "Apples", "Cucumbers", "Reusable bags", "Biscuit", "Peppers", "Nuts", "Cashew Nuts", "Fresh Fruit", "Mixed Nuts", "organic vegetables", "fresh fruits", "Potatoes", "Green pepper", "Onions", "Green Onions", "Mushrooms", "Iceberg", "Carrots", "Tomatoes", "Hot Dog Sausages", "Lays", "Soft Drinks", "Fried chickens", "Pizza", " gamming i5", "Asus TUF f15", "Asus TUF Dash f15", "Acer Nitro 5", "Nvidia GTX 1680", "Nvidia GTX 1680 Ti",
"AMD Radeon RX 6800", "AMD Radeon RX 6700 XT", "AMD Radeon RX 6600 XT", "AMD Radeon RX 5700 XT", "AMD Radeon RX 6800 XT", "AMD Radeon RX 5500 XT", "MSI Radeon RX 6700 XT Gaming X", "AMD Radeon RX 570", "MSI Aero Radeon RX 560", "NVIDIA GeForce RTX 3090", "NVIDIA GeForce RTX 3080 Ti", "NVIDIA GeForce RTX 3080", "NVIDIA GeForce 3080 LHR", "NVIDIA GeForce RTX 2080 Ti", "NVIDIA GeForce RTX 2080", "	NVIDIA GeForce GTX 1080 Ti", "NVIDIA GeForce RTX 2070", "AMD Radeon RX 5600M", "Acer Predator Helios 300", "Lenovo Legion 5 Pro", "Asus ROG Zephyrus G14", "Alienware. m17 R4", "Razer. Blade 15", "Asus ROG Strix Scar 17 G733"]

length = len(product_list)
item_price_list = []
for i in range(length):
   listbox.insert(i, product_list[i])
   rand_price = randint(10, 5000)
   item_price_list.append(rand_price)


no_of_label = Label(
    root, text="no. of items you purchased here :)", font=("aharoni", 15))
no_of_label.pack(pady=10)
no_of_list = Listbox()
x = 0
no_list = []
for i in range(100):
   x += 1
   no_list.append(str(x))
default = StringVar()
default.set("1")
drop = OptionMenu(frame, default, *no_list)
btn_frame = Frame(root)
add_item_btn = Button(btn_frame, text="Add item", bg="#1EE8AB", command=add_item_to_dict)
add_item_btn.pack(side=LEFT, padx=5)








y_scrollbar = Scrollbar(frame, orient='vertical')
y_scrollbar.pack(side=RIGHT, fill=Y)
listbox.config(yscrollcommand=y_scrollbar.set)
y_scrollbar.config(command=listbox.yview)
listbox.pack(side=LEFT)
drop.pack(side=RIGHT)
btn_frame.pack(pady=10)
frame.pack(pady=10)
root.mainloop()