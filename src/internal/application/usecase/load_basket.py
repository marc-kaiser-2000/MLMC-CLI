from abc import ABC, abstractmethod



class LoadBasket(ABC):

    @staticmethod
    @abstractmethod
    def load(path: str) -> None:
        pass


class LoadBasketImpl():

    @staticmethod
    def load(path: str) -> None:
        pass