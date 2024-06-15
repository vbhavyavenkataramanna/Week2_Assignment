class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

class ECommerceWebsite:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_homepage(self):
        print("Welcome to the Beauty Products E-Commerce Website!\n")
        print("Products available:\n")
        for i, product in enumerate(self.products, start=1):
            print(f"{i}. Name: {product.name}")
            print(f"   Price: ${product.price:.2f}")
            print(f"   Description: {product.description}\n")

# Main program
def main():
    # Create an instance of the ECommerceWebsite
    website = ECommerceWebsite()

    # Add products to the website
    website.add_product(Product("Lipstick", 19.99, "A vibrant red lipstick for all occasions."))
    website.add_product(Product("Foundation", 25.50, "A smooth foundation for a flawless finish."))
    website.add_product(Product("Mascara", 15.75, "A waterproof mascara for longer lashes."))
    website.add_product(Product("Blush", 12.00, "A rosy blush for a natural look."))
    website.add_product(Product("Eyeliner", 10.00, "A long-lasting eyeliner for precise application."))

    # Display the homepage
    website.display_homepage()

if __name__ == "__main__":
    main()
