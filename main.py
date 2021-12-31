from tkinter import *
from random import randint
from pprint import pprint

root = Tk()
root.title("Billing App")
root.geometry("550x590")
root.iconbitmap("Resources/logo.ico")

items = []
total_amount_list = []
def add_item_to_dict():
   global item_price_list, items
   
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
   print(items)
   return items
   


def bill_amount():
   global total_amount_list
   item_dict = add_item_to_dict()
   price_list = []
   item_name_list = []
   no_of_items_purchased_list = []
   total = 0
   for i in range(len(item_dict)):
      price = item_dict[i]["price"]
      item_name = item_dict[i]["item name"]
      no_of_products = item_dict[i]["no_of_items"]
      price_list.append(price)
      item_name_list.append(item_name)
      no_of_items_purchased_list.append(no_of_products)
      total_price_for_the_product = price * int(no_of_products)
      total_amount_list.append(total_price_for_the_product)
   for i in total_amount_list:
      total += i
   print(total)
   return total_amount_list

def take_bill():
   data = add_item_to_dict()
   total = bill_amount()
   main_frame.destroy()
   head_label = Label(root, text="Billing App", font=("aharoni", 30))
   head_label.pack(pady=10)
   for i in range(len(data)):
      price = data[i]["price"]
      item_name = data[i]["item name"]
      no_of_products = data[i]["no_of_items"]
      
      item_label = Label(root, text=f"Item name: {item_name} | ", font=("aharoni", 15))
      item_label.pack()




main_frame = Frame(root)
head_label = Label(main_frame, text="Billing App", font=("aharoni", 30))
head_label.pack(pady=10)
entry_label = Label(main_frame, text="Enter The product name :  ", font=("aharoni", 10))
entry_label.pack(pady=5)

list_entry = Entry(main_frame, width=35, font=("aharoni", 10))
list_entry.pack(pady=5)
no_idea = Label(main_frame, text='''No idea on what you buyed ?
here is the list that we have in our shop :)''', font=("aharoni", 10))
no_idea.pack(pady=15)
frame = Frame(main_frame)
inner_frame = Frame(frame, height=45)
listbox = Listbox(inner_frame, width=35, height=15, font=("aharoni", 10))
product_list = ["Bananas", "Water", "Milk", "Beef", "Eggs", "Apples", "Cucumbers", "Reusable bags", "Biscuit", "Peppers", "Nuts", "Cashew Nuts", "Fresh Fruit", "Mixed Nuts", "organic vegetables", "fresh fruits", "Potatoes", "Green pepper", "Onions", "Green Onions", "Mushrooms", "Iceberg", "Carrots", "Tomatoes", "Hot Dog Sausages", "Lays", "Soft Drinks", "Fried chickens", "Pizza", "Lenovo gamming i5", "Asus TUF f15", "Asus TUF Dash f15", "Acer Nitro 5", "Nvidia GTX 1680", "Nvidia GTX 1680 Ti",
"AMD Radeon RX 6800", "AMD Radeon RX 6700 XT", "AMD Radeon RX 6600 XT", "AMD Radeon RX 5700 XT", "AMD Radeon RX 6800 XT", "AMD Radeon RX 5500 XT", "MSI Radeon RX 6700 XT Gaming X", "AMD Radeon RX 570", "MSI Aero Radeon RX 560", "NVIDIA GeForce RTX 3090", "NVIDIA GeForce RTX 3080 Ti", "NVIDIA GeForce RTX 3080", "NVIDIA GeForce 3080 LHR", "NVIDIA GeForce RTX 2080 Ti", "NVIDIA GeForce RTX 2080", "	NVIDIA GeForce GTX 1080 Ti", "NVIDIA GeForce RTX 2070", "AMD Radeon RX 5600M", "Acer Predator Helios 300", "Lenovo Legion 5 Pro", "Asus ROG Zephyrus G14", "Alienware. m17 R4", "Razer. Blade 15", "Asus ROG Strix Scar 17 G733"]

length = len(product_list)
item_price_list = []
for i in range(length):
   listbox.insert(i, product_list[i])
   rand_price = randint(10, 5000)
   item_price_list.append(rand_price)


no_of_label = Label(
    frame, text="no. of items you purchased here :)", font=("aharoni", 10))

no_of_list = Listbox()
x = 0
no_list = []
for i in range(100):
   x += 1
   no_list.append(str(x))
default = StringVar()
default.set("1")
drop = OptionMenu(frame, default, *no_list)
btn_frame = Frame(main_frame)
add_item_btn = Button(btn_frame, text="Add item", bg="#1EE8AB", command=add_item_to_dict)
calculate_item_btn = Button(btn_frame, text="Take Bill", bg="#1EE8AB", command=take_bill)
calculate_item_btn.pack(side=RIGHT, padx=20)


y_scrollbar = Scrollbar(inner_frame, orient='vertical')
y_scrollbar.pack(side=RIGHT, fill=Y)
listbox.config(yscrollcommand=y_scrollbar.set)
y_scrollbar.config(command=listbox.yview)

listbox.pack(side=LEFT)
drop.pack(side=RIGHT, padx=20)
no_of_label.pack(pady=10, side=RIGHT)



inner_frame.pack(pady=10)
add_item_btn.pack(side=LEFT, padx=5)
inner_frame.pack()
frame.pack(pady=10)
btn_frame.pack(pady=10)
main_frame.pack()
root.mainloop()