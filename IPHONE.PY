# ==============================================
# iPhone.py
# Simple iPhone information app (CLI version)
# Author: Your Name
# For GitHub project
# ==============================================

class iPhone:
    def __init__(self, model, storage, ios_version, price):
        self.model = model
        self.storage = storage
        self.ios_version = ios_version
        self.price = price

    def info(self):
        print("====================================")
        print("        📱 iPhone Information        ")
        print("====================================")
        print(f"Model:        {self.model}")
        print(f"Storage:      {self.storage}")
        print(f"iOS Version:  {self.ios_version}")
        print(f"Price:        ${self.price}")
        print("====================================")


def main():
    print("Welcome to iPhone.py!")
    print("Choose an iPhone model:\n")

    phones = {
        "1": iPhone("iPhone 14 Pro", "256GB", "iOS 17", 1199),
        "2": iPhone("iPhone 15", "128GB", "iOS 17", 899),
        "3": iPhone("iPhone SE (2022)", "64GB", "iOS 16", 429),
    }

    for key in phones:
        print(f"{key}. {phones[key].model}")

    choice = input("\nEnter number: ")

    if choice in phones:
        phones[choice].info()
    else:
        print("❌ Wrong selection!")

if __name__ == "__main__":
    main()

