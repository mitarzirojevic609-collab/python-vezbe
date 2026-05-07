import tkinter as tk
from PIL import ImageTk, Image
window = tk.Tk()
window.geometry("1024x768")
window.title("Lista proizvoda")

fruits_info = {
    "Apple": "Apple is a sweet fruit that can be red or green.",
    "Banana": "Banana is a long yellow fruit that is very sweet.",
    "Cherry": "Cherry is a small red fruit with a sweet or sour taste.",
    "Date": "Date is a brown fruit that is very sweet and grows in hot climates.",
    "Elderberry": "Elderberry is a small dark purple fruit often used in juices and medicine."
}

fruit_images ={
    "Apple": "jabuka.jpeg",
    "Banana": "banana.jpeg"

}

def show_item_info(event):
    selection = listbox.curselection()
    name = listbox.get(selection)

    product_info.configure(state="normal")

    image = Image.open(fruit_images[name])
    image = image.resize((50, 50))

    photo = ImageTk.PhotoImage(image)



    product_info.delete('1.0', tk.END)
    product_info.insert(tk.END, fruits_info[name])

    image_label.configure(image=photo)
    image_label.image = photo

    product_info.configure(state="disabled")

product_list = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]


listbox = tk.Listbox(window, height=50)
listbox.pack(side="left", padx=10)

for item in product_list:
    listbox.insert(tk.END, item)

listbox.bind("<<ListboxSelect>>", show_item_info)

product_info = tk.Text(window, width=50, height=50, font=("Arial", 14))
product_info.pack(side="left")

image_label = tk.Label(window, bg="white", width=50, height=50)
image_label.pack(side="left", padx=20)

window.mainloop()