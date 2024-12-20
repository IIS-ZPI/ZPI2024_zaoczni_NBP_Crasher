from abc import ABC, abstractmethod


class Arithmetics(ABC):
    # Test 1
    @abstractmethod
    def addition(self, a: float, b: float) -> float:
        pass

    @abstractmethod
    def difference(self, a: float, b: float) -> float:
        pass

    @abstractmethod
    def multiplication(self, a: float, b: float) -> float:
        pass
    
    @abstractmethod
    def power(self, a: float, b: float) -> float:
        pass
    
    # Divide method implementation 
    @abstractmethod
    def divide(self, a: float, b: float) -> float:
        pass
