class NameTooShortError(Exception):
    """The username is less or equal 4 character"""
    pass

class MustContainAtSymbolError(Exception):
    """Missing @ symbol"""
    pass

class InvalidDomainError(Exception):
    """Domain is not in the valid domains"""
    pass