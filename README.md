# Movie-Trailer-Website

Udaicty Full Stack Nanodegree's 1st Project, to build a movie trailer website

## Content

### Media 
this file contians the class **Movie** which contains the instructor `def __init__():` with all the variable instances as shown below:

` 	self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.rating_on_idmb = movie_rating_on_idmb
		self.category = movie_category
` 
along with an instance method **show_trailer** which allows the program to open the webbrowser and access the provided youtube URLs:

` 
def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
` 

### Entertainment_Center
this file imported the media file to use the class **Movive**, it is calling the constructor `media.Movie()` to instantiate movie objects

Sample:
` the_nun = media.Movie("The Nun (2018)", "A priest with a haunted past.",
 "https://upload.wikimedia.org/wikipedia/en/3/34/TheNunPoster.jpg",
  "https://www.youtube.com/watch?v=zwAM5UnGd2s&ab_channel=FilmSelectTrailer", 
  "5.6/10", "Horor")
  `
  
  
