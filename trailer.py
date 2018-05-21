#!/usr/bin/env python
import media
import fresh_tomatoes
print("content-type:text/html \n")
spiderman1 = media.Movie("spider man-1",
                         "https://bit.ly/2GD3KRc",
                         "https://www.youtube.com/embed/TYMMOjBUPMM")
# print(spider man-1.storyline)
spiderman2 = media.Movie("spider man-2",
                         "https://bit.ly/2KCR8Mk",
                         "https://www.youtube.com/embed/BWsLc3j1AWg")

Amazing_spiderman = media.Movie("Amazing spider man",
                                "https://bit.ly/2wXjr6l",
                                "https://www.youtube.com/embed/-tnxzJ0SSOw")

Spiderman_homecoming = media.Movie("Spider man home coming",
                                   "https://bit.ly/2Ivqngi",
                                   "https://www.youtube.com/embed/n9DwoQ7HWvI")

Spiderman_homecoming_2 = media.Movie("Spider man home coming-2",
                                     "https://bit.ly/2s0z5YO",
                                     "https://www.youtube.com"
                                     "/embed/8QYZQiBVx18")
# (spider man-1.show_trailer())
movies = [spiderman1, spiderman2,
          Amazing_spiderman, Spiderman_homecoming, Spiderman_homecoming_2]
fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.__doc__)

