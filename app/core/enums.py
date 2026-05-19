from enum import Enum

class TokenType(Enum):
    ACCESS_TOKEN_EXPIRE_MINUTES = 15
    REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7
    ALGORITHM = "HS256"
    
