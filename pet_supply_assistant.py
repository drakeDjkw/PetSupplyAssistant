class PetSupplyAssistant:
    def __init__(self):
        self.pets = {}

    def add_pet(self, name, type_of_pet, age):
        self.pets[name] = {'type': type_of_pet, 'age': age}
        print(f"Added {name}, a {age}-year-old {type_of_pet}!")

    def recommend_products(self, name):
        if name not in self.pets:
            print("Pet not found!")
            return

        pet_info = self.pets[name]
        recommendations = []

        if pet_info['type'].lower() == 'dog':
            recommendations = ["Dog Food", "Dog Toys", "Dog Grooming Supplies"]
        elif pet_info['type'].lower() == 'cat':
            recommendations = ["Cat Food", "Cat Litter", "Cat Toys"]
        
        print(f"Recommended products for {name}: {', '.join(recommendations)}")

    def run(self):
        while True:
            action = input("Choose an action: add_pet / recommend / exit: ")
            if action.lower() == 'add_pet':
                name = input("Enter the pet's name: ")
                type_of_pet = input("Enter the type of pet (dog/cat): ")
                age = input("Enter the pet's age: ")
                self.add_pet(name, type_of_pet, age)
            elif action.lower() == 'recommend':
                name = input("Enter the pet's name for recommendations: ")
                self.recommend_products(name)
            elif action.lower() == 'exit':
                print("Exiting the assistant. Goodbye!")
                break
            else:
                print("Invalid action. Please try again.")

if __name__ == "__main__":
    assistant = PetSupplyAssistant()
    assistant.run()