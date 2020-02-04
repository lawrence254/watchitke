# from app import app
import urllib.request,json
from .models import Movie

api_key = None
base_url = None


def configure_request(app):
    global api_key,base_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['BASE_URL']

# Movie = movie.Movie

def get_movies(category):
    get_movies_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_results = None

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results=process_results(movie_results_list)

    return movie_results

def get_movie(mId):
    get_movie_details_url = base_url.format(mId,api_key)
    print(get_movie_details_url)

    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        movie_object = None
        
        if movie_details_response:
            mId = movie_details_response.get('id')
            title = movie_details_response.get('original_title')
            overview = movie_details_response.get('overview')
            poster = movie_details_response.get('poster_path')
            background = movie_details_response.get('backdrop_path')
            vote_average = movie_details_response.get('vote_average')
            vote_count = movie_details_response.get('vote_count')

            movie_object = Movie(mId,title,overview,poster,background,vote_average,vote_count)

    return movie_object
    
def search_movie(movie_name):
    search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,movie_name)
    with urllib.request.urlopen(search_movie_url) as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_movie_data)
        
        search_movie_results = None
        if search_movie_response['results']:
            search_movie_list = search_movie_response['results']
            search_movie_results = process_results(search_movie_list)

    return search_movie_results

def process_results(movie_list):
    movie_results = []
    for movie_item in movie_list:
        title = movie_item.get('original_title')
        mId = movie_item.get('id')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        background = movie_item.get('backdrop_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster:
            movie_object = Movie(mId,title,overview,poster,background,vote_average,vote_count)
            movie_results.append(movie_object)

    return movie_results
