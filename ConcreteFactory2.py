from AbstractFactory import AbstractFactory
from AbstractProductA import AbstractProductA
from AbstractProductB import AbstractProductB
from ConcreteProductA2 import ConcreteProductA2
from ConcreteProductB2 import ConcreteProductB2


class ConcreteFactory2(AbstractFactory):
    """
    Each Concrete Factory has a corresponding product variant.
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()