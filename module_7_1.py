# Режимы открытия файлов
# Задача  "Учёт товаров"

class Product:                             # продукт
    def __init__(self, name, weight, category):
        self.name = name                    # название продукта (строка)
        # общий вес товара (дробное число) (5.4, 52.8 и т.п.).
        self.weight = weight
        self.category = category            # атегория товара (строка)

# возвращает строку в формате '<название>, <вес>, <категория>'
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:                                  # магазин
    def __init__(self):
        self.__file_name = 'products.txt'

# считывает всю информацию из файла __file_name и возвращает единую строку со всеми товарами из файла
    def get_products(self):
        file = open(self.__file_name, 'r')
        sp_pr = file.read()
        file.close()
        return sp_pr

 # Принимает неограниченное количество объектов класса Product.
 # Добавляет в файл продукт из products, если его ещё нет в файле
    def add(self, *products):
        for product in products:
            list_of_products = self.get_products()
            if product.__str__() in list_of_products:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{product}\n')
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())
