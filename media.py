

import webbrowser

class Movie():
    

    def __init__(temp, movie_title, movie_overview, poster_image, trailer_youtube):
        temp.title = movie_title
        temp.movie_overview = movie_overview
        temp.poster_image_url = poster_image
        temp.trailer_youtube_url = trailer_youtube

    def show_trailer(temp):
        webbrowser.open(temp.trailer_youtube_url)
