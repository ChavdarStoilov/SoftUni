class Catalogue:
    products = []

    def __init__(self, name: str):
        self.name = name

    def add_product(self, product_name: str):
        self.product_name = product_name
        Catalogue.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [letter for letter in Catalogue.products if first_letter in letter]

    def __repr__(self):
        test = '\n'.join(sorted(Catalogue.products))

        return f"Items in the {self.name} catalogue:\n" \
               f"{test}"

