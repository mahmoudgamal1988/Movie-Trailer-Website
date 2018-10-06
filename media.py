#importing webbrowser module which allows to open web links.
import webbrowser

class Movie():
	""""a calss which we use to provide movies' data """
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_rating_on_idmb, movie_category):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.rating_on_idmb = movie_rating_on_idmb
		self.category = movie_category

'''an instance method with the function show_trailer,
which allows accessing the provided youtube links.'''
def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)






