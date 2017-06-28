import media
import fresh_tomatoes

# Following are the objects created of class Movie.
harry_potter2 = media.Movie("Harry Potter",
                            "Story of Harry Potters second year at Hogwarts",
                            "https://upload.wikimedia.org/wikipedia/en/c/c0/Harry_Potter_and_the_Chamber_of_Secrets_movie.jpg", # NOQA
                            "https://www.youtube.com/watch?v=dmPrfYkpwTY")


avatar = media.Movie("AVATAR",
                     "A marine on an alien planet", 
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", # NOQA
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

kung_fu_panda = media.Movie("KungFu Panda",
                            "A panda becomes a kungfu warrior", 
                            "https://upload.wikimedia.org/wikipedia/en/thumb/7/76/Kungfupanda.jpg/220px-Kungfupanda.jpg", # NOQA
                            "https://www.youtube.com/watch?v=PXi3Mv6KMzY")

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life", 
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

cars = media.Movie("CARS",
                     "A world populated by anthramorphic cars", 
                     "https://upload.wikimedia.org/wikipedia/en/3/34/Cars_2006.jpg",# NOQA
                     "https://www.youtube.com/watch?v=uxx75HVd-F0")

spiderman = media.Movie("SPIDERMAN",
                     "A student develops Spider like super powers", 
                     "https://upload.wikimedia.org/wikipedia/en/f/f3/Spider-Man2002Poster.jpg", # NOQA
                     "https://www.youtube.com/watch?v=O7zvehDxttM")


# a list of all the objects created of movies is created
movies = [harry_potter2, avatar, kung_fu_panda, toy_story, cars, spiderman]
# As open_movies_page in fresh_tomatoes takes list as a parameter 
# therfore we need to pass moviesas a parameter
fresh_tomatoes.open_movies_page(movies)

