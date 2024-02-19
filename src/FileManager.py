import json
from abc import ABC, abstractmethod


class FileManager(ABC):
    @abstractmethod
    def add_to_file(self, path, vacancies):
        pass

    @abstractmethod
    def read_file(self, path):
        pass

    @abstractmethod
    def delete_from_file(self, path):
        pass




