import webbrowser
print("content-type:text/html \n")


class Movie():
                """The attributes of movie trailer are:
                Attributes:
                movie_title:Specifies movie title.
                poster_image:gives movie poster.
                trailer_youtube:gives youtube link.
                """
                VALID_RATINGS = ["EXCELLENT", "GOOD", "BAD", "AVERAGE"]

                def __init__(self, movie_title, poster_image, trailer_youtube):
                                self.title = movie_title
                                self.poster_image_url = poster_image
                                self.trailer_youtube_url = trailer_youtube

                def show_trailer(self):
                    webbrowser.open(self.trailer_youtube_url)
