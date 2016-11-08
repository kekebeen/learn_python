import webbrowser
class Movie():
    """ Movie table definition"""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.movie_title = movie_title
        self.movie_storyline = movie_storyline
        self.poster_image = poster_image
        self.trailer_youtube = trailer_youtube
    def show_trailer(self):
        """ opens movie trailer in new tab """
        webbrowser.open(self.trailer_youtube)
