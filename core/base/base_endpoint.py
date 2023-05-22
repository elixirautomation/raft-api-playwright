from abc import ABC, abstractmethod


class IEndpointTemplate(ABC):
    @abstractmethod
    def url(self) -> str:
        pass

    @abstractmethod
    def http_method(self) -> str:
        pass

    @abstractmethod
    def query_parameters(self) -> dict | None:
        pass

    @abstractmethod
    def path_parameters(self, **kwargs) -> dict | None:
        pass

    @abstractmethod
    def headers(self) -> dict:
        pass

    @abstractmethod
    def request_body(self) -> dict | None:
        pass
