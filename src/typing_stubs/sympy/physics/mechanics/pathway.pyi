import abc
from abc import ABC, abstractmethod

__all__ = ['PathwayBase', 'LinearPathway', 'ObstacleSetPathway', 'WrappingPathway']

class PathwayBase(ABC, metaclass=abc.ABCMeta):
    def __init__(self, *attachments) -> None: ...
    @property
    def attachments(self): ...
    @attachments.setter
    def attachments(self, attachments) -> None: ...
    @property
    @abstractmethod
    def length(self): ...
    @property
    @abstractmethod
    def extension_velocity(self): ...
    @abstractmethod
    def to_loads(self, force): ...

class LinearPathway(PathwayBase):
    def __init__(self, *attachments) -> None: ...
    @property
    def length(self): ...
    @property
    def extension_velocity(self): ...
    def to_loads(self, force): ...

class ObstacleSetPathway(PathwayBase):
    def __init__(self, *attachments) -> None: ...
    @property
    def attachments(self): ...
    @attachments.setter
    def attachments(self, attachments) -> None: ...
    @property
    def length(self): ...
    @property
    def extension_velocity(self): ...
    def to_loads(self, force): ...

class WrappingPathway(PathwayBase):
    def __init__(self, attachment_1, attachment_2, geometry) -> None: ...
    @property
    def geometry(self): ...
    @geometry.setter
    def geometry(self, geometry) -> None: ...
    @property
    def length(self): ...
    @property
    def extension_velocity(self): ...
    def to_loads(self, force): ...
