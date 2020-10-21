from AbstractFactory import AbstractFactory
from AbstractProductA import AbstractProductA
from AbstractProductB import AbstractProductB
from ConcreteProductA1 import ConcreteProductA1
from ConcreteProductB1 import ConcreteProductB1


class ConcreteFactory1(AbstractFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()