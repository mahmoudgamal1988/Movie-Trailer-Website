#import the media file which contains the Movie class.
import media

#import fresh_tomatoes file whoch contains the HTML, CSS & JS codes.
import fresh_tomatoes

'''the below code contains the instance variable of the class movie,
 which provies the needed details such as:
Movie Name & the release year,
Movie Story Line, A link for the movie's poster,
A Youtube link for the movie's trailer, IDMB movie's rating,
and the movie's category '''

the_nun = media.Movie(
	"The Nun (2018)",
	"The plot follows a Roman Catholic priest and a nun in her novitiate.",
	"https://bit.ly/2xZaE1Z",
	"https://www.youtube.com/watch?v=pzD9zGcUNrw&ab_channel=WarnerBros.Pictures",
	"5.6/10","Horor"
	)

fury = media.Movie(
	"Fury (2014)",
	"Grizzled tank commander and his crew fight their way across Germany.",
	"https://bit.ly/2zWfAGi",
	"https://www.youtube.com/watch?v=DNHuK1rteF4&ab_channel=MovieclipsTrailers",
	"7.6/10","Action , Drama , War"
	)


war_for_the_planet_of_apes = media.Movie(
	"War for the Planet of the Apes (2017)",
	"Caesarand his apes are forced into a deadly conflict with an army of humans.",
	"https://bit.ly/2yhWicn",
	"https://www.youtube.com/watch?v=qxjPjPzQ1iU&t=15s&ab_channel=PlanetoftheApes","7.5/10",
	" Action , Adventure , Drama"
	)


blackhat = media.Movie(
	"Blackhat (2015)",
	"A furloughed convict and his American and Chinese partners hunt a high-level cybercrime network from Chicago to Los Angeles to Hong Kong to Jakarta.",
	"https://bit.ly/2ODll3K",
	"https://www.youtube.com/watch?v=jZ1ZDlLImF8&ab_channel=MovieclipsComingSoon",
	"5.4/10","Action , Crime , Thriller"
	)


edge_of_tomorrow = media.Movie(
	"Edge of Tomorrow (2014)",
	"A soldier fighting aliens gets to relive the same day over and over again, the day restarting every time he dies.",
	"https://bit.ly/2NsrET9",
	"https://www.youtube.com/watch?v=vw61gCe2oqI&ab_channel=WarnerBros.Pictures",
	"7.9/10","Action , Adventure , Sci-Fi"
	)

train_to_busan = media.Movie(
	"Train to Busan (2016)",
	"While a zombie virus breaks out in South Korea, passengers struggle to survive on the train from Seoul to Busan.",
	"https://bit.ly/2OF9MsB",
	"https://www.youtube.com/watch?v=1d4DACwz49o&ab_channel=ZeroMedia",
	"7.9/10","Action , Horror , Thriller"
	)

'''
the movies var which has all the instance variables to be used at the following function,
which will allow the HTML displays all of the provided movies data
'''
movies = [the_nun,
fury,
war_for_the_planet_of_apes,
blackhat,
edge_of_tomorrow,
train_to_busan]

'''function that will take inthe  list of movies and generate an HTML file including this content,
producing a website to showcase your favorite movies.'''
fresh_tomatoes.open_movies_page(movies)
