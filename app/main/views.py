from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_movies,get_movie,search_movie,get_tv,get_show
from .forms import ReviewForm
from ..models import Review

# Review = review.Review

#Views
@main.route('/')
def index():
    '''
    Returns index page including its data
    '''
    popular_movies = get_movies('popular')
    upcoming_movies = get_movies('upcoming')
    now_showing_movies = get_movies('now_playing')
        
    search_movie = request.args.get('movie_query')
    title = 'Home of The Best Online Movies Aggregator'
    if search_movie:
        return redirect(url_for('main.search',movie_name=search_movie))
    return render_template('index.html', title=title, popular = popular_movies, upcoming= upcoming_movies, now_showing = now_showing_movies)

@main.route('/movie/<int:mId>')
def movie(mId):
    '''
    Single movie view page
    '''
    movie = get_movie(mId)
    title = f'{movie.title}'
    reviews = Review.get_reviews(movie.mId)

    return render_template('movie.html', movie = movie,title = title,reviews = reviews)

@main.route('/search/<movie_name>')
def search(movie_name):
    '''
    View function to display the search results
    '''
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'
    return render_template('search.html',movies = searched_movies)

@main.route('/movie/review/new/<int:mId>', methods = ['GET','POST'])
def new_review(mId):
    form = ReviewForm()
    movie = get_movie(mId)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(movie.mId,title,movie.poster,review)
        new_review.save_review()
        return redirect(url_for('main.movie',mId =mId ))

    title = f'{movie.title} review'
    return render_template('new_review.html',title = title, review_form=form, movie=movie)




@main.route('/tv')
def get_series():
    '''
    Returns index page including its data
    '''
    popular_tv = get_tv('popular')
    top_rated_tv = get_tv('top_rated')
    now_showing_tv = get_tv('on_the_air')
        
    search_tv = request.args.get('tv_query')
    title = 'Home of The Best Online Movies Aggregator'
    if search_tv:
        return redirect(url_for('main.search',show_name=search_tv))
    return render_template('series.html', title=title, popular = popular_tv, top_rated = top_rated_tv, now_showing = now_showing_tv)

@main.route('/show/<int:mId>')
def show(mId):
    '''
    Single movie view page
    '''
    show_id = get_show(mId)
    # show_title = f'{show.title}'
    # reviews = Review.get_reviews(movie.mId)

    return render_template('show.html', show = show_id)