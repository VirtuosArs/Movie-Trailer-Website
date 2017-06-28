import webbrowser

# This is a Movie class that defines a set of attributes that characterize any object of the class
class Movie():
    """ This class provides a way to store movie related information """

    
    # It is a class variable and are shared by all instances of a class
    VALID_RATINGS = ["G", "PG", "PG-12", "R"]
    
    # All the following variables in the function are known as insance variables
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
