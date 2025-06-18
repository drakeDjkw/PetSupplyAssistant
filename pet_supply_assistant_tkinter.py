import tkinter as tk
from tkinter import messagebox


class PetSupplyAssistant:
    def __init__(self, master):
        self.master = master
        master.title("Pet Supply Assistant")

        self.pets = {}

        self.label = tk.Label(master, text="Pet Name:")
        self.label.pack()

        self.pet_name_entry = tk.Entry(master)
        self.pet_name_entry.pack()

        self.type_label = tk.Label(master, text="Type of Pet (dog/cat):")
        self.type_label.pack()

        self.pet_type_entry = tk.Entry(master)
        self.pet_type_entry.pack()

        self.age_label = tk.Label(master, text="Age of Pet:")
        self.age_label.pack()

        self.pet_age_entry = tk.Entry(master)
        self.pet_age_entry.pack()

        self.add_pet_button = tk.Button(master, text="Add Pet", command=self.add_pet)
        self.add_pet_button.pack()

        self.recommend_button = tk.Button(master, text="Get Recommendations", command=self.recommend_products)
        self.recommend_button.pack()

    def add_pet(self):
        name = self.pet_name_entry.get()
        type_of_pet = self.pet_type_entry.get()
        age = self.pet_age_entry.get()
        
        if name and type_of_pet and age:
            self.pets[name] = {'type': type_of_pet, 'age': age}
            messagebox.showinfo("Success", f"Added {name}, a {age}-year-old {type_of_pet}!")
            # Clear the input fields
            self.pet_name_entry.delete(0, tk.END)
            self.pet_type_entry.delete(0, tk.END)
            self.pet_age_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")

    def recommend_products(self):
        name = self.pet_name_entry.get()
        
        if name not in self.pets:
            messagebox.showwarning("Not Found", "Pet not found!")
            return

        pet_info = self.pets[name]
        
        if pet_info['type'].lower() == 'dog':
            recommendations = ["Dog Food", "Dog Toys", "Dog Grooming Supplies"]
        elif pet_info['type'].lower() == 'cat':
            recommendations = ["Cat Food", "Cat Litter", "Cat Toys"]
        
        messagebox.showinfo("Recommendations", f"Recommended products for {name}: {', '.join(recommendations)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PetSupplyAssistant(root)
    root.mainloop()