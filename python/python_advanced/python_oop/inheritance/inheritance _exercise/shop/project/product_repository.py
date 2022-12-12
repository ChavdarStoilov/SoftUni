class ProductRepository:

    def __init__(self, products = []):
        self.products = products


    def add(self, product):
        self.products.append(product)

    def find(self, product_name: str):
        
        for product in self.products:
            if product.name == product_name:
                return product
        

    def remove(self, product_name):
        
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)

    def __repr__(self):
        
        products_list = ''

        for product in self.products:
            products_list += f'{product.name}: {product.quantity}\n'

        return products_list.strip()