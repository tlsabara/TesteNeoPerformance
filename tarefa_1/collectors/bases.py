from abc import ABC, abstractmethod
from turtle import pd
from typing import Any


class BaseCollector(ABC):

    @abstractmethod
    def _load(self) -> None:
        ...

    @abstractmethod
    def _transform(self) -> None:
        ...

    @abstractmethod
    def _export(self) -> Any:
        ...

    def run(self) -> Any:
        self._load()
        self._transform()
        return self._export()

