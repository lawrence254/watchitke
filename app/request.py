# from app import app
import urllib.request,json
from .models import Movie,TV

api_key = None
base_url = None
tv_base_url = None


def configure_request(app):
    global api_key,base_url,tv_base_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['BASE_URL']
    tv_base_url = app.config['TV_BASE_URL']

# Movie = movie.Movie

def get_movies(category):
    get_movies_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_results = None

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            

            movie_results = process_results(movie_results_list)
    return movie_results

def get_movie(mId):
    get_movie_details_url = base_url.format(mId,api_key)
   

    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        movie_object = None
        
        if movie_details_response:
            mId = movie_details_response.get('id')
            title = movie_details_response.get('original_title')
            overview = movie_details_response.get('overview')
            poster = movie_details_response.get('poster_path')
            production = movie_details_response.get('production_companies')
            background = movie_details_response.get('backdrop_path')
            vote_average = movie_details_response.get('vote_average')
            vote_count = movie_details_response.get('vote_count')

            movie_object = Movie(mId,title,overview,poster,background,vote_average,vote_count)
            movie_object.production = production

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
        production = movie_item.get('production_companies')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        background = movie_item.get('backdrop_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster and background:
            movie_object = Movie(mId,title,overview,poster,background,vote_average,vote_count)
            movie_results.append(movie_object)

    return movie_results


# TV/SERIES
def get_tv(category):
    get_tv_url = tv_base_url.format(category,api_key)
    with urllib.request.urlopen(get_tv_url) as url:
        get_tv_data = url.read()
        get_tv_response = json.loads(get_tv_data)
        # print(get_tv_response)

        tv_results = None

        if get_tv_response['results']:
            tv_results_list = get_tv_response['results']
            # print(tv_results_list)

            tv_results = process_results(tv_results_list)
    return tv_results


def get_show(mId):
    get_show_details_url = tv_base_url.format(mId,api_key)
   

    with urllib.request.urlopen(get_show_details_url) as url:
        show_details_data = url.read()
        show_details_response = json.loads(show_details_data)

        shows_object = None
        
        if show_details_response:
            mId = show_details_response.get('id')
            title = show_details_response.get('original_title')
            overview = show_details_response.get('overview')
            poster = show_details_response.get('poster_path')
            production = show_details_response.get('production_companies')
            background = show_details_response.get('backdrop_path')
            vote_average = show_details_response.get('vote_average')
            first_air_date = show_details_response.get('last_air_date')

            shows_object = TV(mId,title,overview,poster,background,vote_average,first_air_date)
            # show_object.production = production

        return shows_object

def process_tv_results(tv_results_list):
    series_results = []
    for tv_item in tv_results_list:
        name = tv_item.get('original_name')
        mId = tv_item.get('id')
        overview = tv_item.get('overview')
        poster = tv_item.get('poster_path')
        background = tv_item.get('backdrop_path')
        vote_average = tv_item.get('vote_average')
        first_air_date = tv_item.get('first_air_date')

        if poster and background:
            series_object = TV(mId,name,overview,poster,background,vote_average,first_air_date)
            series_results.append(series_object)

    return series_results