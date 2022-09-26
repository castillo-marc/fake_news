import os

class Config:
    DEBUG=False
    DEVELOPMENT=False

class ProductionConfig(Config):
    pass

class StagingConfig(Config):
    DEBUG=True

class DevelopmentConfig(Config):
    DEBUG=True
    DEVELOPMENT=True