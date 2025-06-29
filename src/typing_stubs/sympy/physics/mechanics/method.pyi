import abc
from abc import ABC, abstractmethod

class _Methods(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def q(self): ...
    @abstractmethod
    def u(self): ...
    @abstractmethod
    def bodies(self): ...
    @abstractmethod
    def loads(self): ...
    @abstractmethod
    def mass_matrix(self): ...
    @abstractmethod
    def forcing(self): ...
    @abstractmethod
    def mass_matrix_full(self): ...
    @abstractmethod
    def forcing_full(self): ...
