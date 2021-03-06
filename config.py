import os

class Config:
    BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    TV_BASE_URL = 'https://api.themoviedb.org/3/tv/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    pass
class ProdConfig(Config):
    '''
    Production config child class
    
    Args: 
        Config: The parent configuration class with General configuration settings
    '''
    pass
class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
 
    '''


    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}