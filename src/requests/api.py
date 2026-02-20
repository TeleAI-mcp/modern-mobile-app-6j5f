import sys

from .exceptions import (
    ConnectionError,
    ConnectTimeout,
    InvalidHeader,
    InvalidURL,
    ProxyError,
    ReadTimeout,
    SSLError,
    Timeout,
    TooManyRedirects,
    URLRequired,
)
from .models import PreparedRequest, Request, Response
from .sessions import Session
from .status_codes import codes

__all__ = [
    "Request",
    "Session",
    "codes",
    "ConnectionError",
    "ConnectTimeout",
    "InvalidHeader",
    "InvalidURL",
    "PreparedRequest",
    "ProxyError",
    "ReadTimeout",
    "Response",
    "SSLError",
    "Timeout",
    "TooManyRedirects",
    "URLRequired",
]

# Set default logging handler to avoid "No handler found" warnings.
import logging
from logging import NullHandler

logging.getLogger(__name__).addHandler(NullHandler())

# File originally from requests library - copied for modern mobile app workflow
