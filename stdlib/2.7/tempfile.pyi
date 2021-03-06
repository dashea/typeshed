# Stubs for tempfile
# Ron Murawski <ron@horizonchess.com>

# based on http://docs.python.org/3.3/library/tempfile.html
# Adapted for Python 2.7 by Michal Pokorny

# TODO: Don't use basestring. Use Union[str, bytes] or AnyStr for arguments.
#       Avoid using Union[str, bytes] for return values, as it implies that
#       an isinstance() check will often be required, which is inconvenient.

from typing import Tuple, IO

# global variables
tempdir = ...  # type: str
template = ...  # type: str

# TODO text files

# function stubs
def TemporaryFile(
            mode: basestring = ..., bufsize: int = ..., suffix: basestring = ...,
            prefix: basestring = ..., dir: basestring = ...) -> IO[str]: ...
def NamedTemporaryFile(
            mode: basestring = ..., bufsize: int = ..., suffix: basestring = ...,
            prefix: basestring = ..., dir: basestring = ..., delete: bool = ...
            ) -> IO[str]: ...
def SpooledTemporaryFile(
           max_size: int = ..., mode: basestring = ..., buffering: int = ...,
           suffix: basestring = ..., prefix: basestring = ..., dir: basestring = ...) -> IO[str]:
    ...

class TemporaryDirectory:
    name = ...  # type: basestring
    def __init__(self, suffix: basestring = ..., prefix: basestring = ...,
                 dir: basestring = ...) -> None: ...
    def cleanup(self) -> None: ...
    def __enter__(self) -> basestring: ...
    def __exit__(self, type, value, traceback) -> bool: ...

def mkstemp(suffix: basestring = ..., prefix: basestring = ..., dir: basestring = ...,
            text: bool = ...) -> Tuple[int, basestring]: ...
def mkdtemp(suffix: basestring = ..., prefix: basestring = ...,
            dir: basestring = ...) -> basestring: ...
def mktemp(suffix: basestring = ..., prefix: basestring = ...,
           dir: basestring = ...) -> basestring: ...
def gettempdir() -> basestring: ...
def gettempprefix() -> basestring: ...
