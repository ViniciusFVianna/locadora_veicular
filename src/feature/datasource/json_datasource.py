from abc import ABC, abstractmethod

class JsonDataSource(ABC):

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def save_data(self, data):
        pass