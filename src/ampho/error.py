"""Ampho Errors
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class AmphoError(Exception):
    """Base Ampho error
    """
    pass


class BundleError(AmphoError):
    """Bundle's module is not found
    """

    def __init__(self, name: str):
        self._name = name


class BundleImportError(BundleError):
    """Error while
    """

    def __str__(self) -> str:
        return f"Bundle's module '{self._name}' cannot be imported"


class BundleNotRegisteredError(BundleError):
    """Bundle with the specified name is not registered
    """

    def __str__(self) -> str:
        return f"Bundle '{self._name}' is not registered"


class BundleAlreadyRegisteredError(BundleError):
    """Bundle with the same name is already registered
    """

    def __str__(self) -> str:
        return f"Bundle '{self._name}' is already registered"
