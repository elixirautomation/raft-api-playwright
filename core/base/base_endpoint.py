"""
This will act like a template for further request processing.
"""
from abc import ABC, abstractmethod


class IEndpointTemplate(ABC):
    @abstractmethod
    def url(self) -> str:
        """
        This function is used for fetching the endpoint.
        :return: it will return the endpoint string.
        """
        pass

    @abstractmethod
    def http_method(self) -> str:
        """
        This method is used for fetching the http method to process.
        :return: it returns the http method name.
        """
        pass

    @abstractmethod
    def query_parameters(self) -> dict | None:
        """
        This method is used to pass the query parameters.
        :return: it returns the parameter dictionary.
        """
        pass

    @abstractmethod
    def path_parameters(self, **kwargs) -> dict | None:
        """
        This method is used to pass the path parameters.
        :param kwargs: here we can pass the path parameter values
        which can further passed to endpoint formats
        :return: it returns the dictionary of path parameter values
        """
        pass

    @abstractmethod
    def headers(self) -> dict:
        """
        This method is used to pass the request headers.
        :return: it returns the dictionary of request headers.
        """
        pass

    @abstractmethod
    def request_body(self) -> dict | None:
        """
        This method is used to pass the request body.
        :return: it returns the dictionary of request body.
        """
        pass
