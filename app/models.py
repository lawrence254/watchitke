class Movie:
    def __init__(self, mId, title,overview,poster,background,vote_average,vote_count):
        self.mId = mId
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+poster
        self.background = 'https://image.tmdb.org/t/p/original/'+ background
        self.vote_average =vote_average
        self.production = 'production'
        self.vote_count = vote_count

class TV:
    def __init__(self, mId, name,overview,poster,background,vote_average,first_air_date):
        self.mId = mId
        self.name = name
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+poster
        self.background = 'https://image.tmdb.org/t/p/original/'+ background
        self.vote_average =vote_average
        self.first_air_date = first_air_date

class Review:

    all_reviews = []

    def __init__(self,mId,title,imageurl,review):
        self.mId = mId
        self.title = title
        self.imageurl = imageurl
        self.review = review


    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.mId == id:
                response.append(review)

        return response