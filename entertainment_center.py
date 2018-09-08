

import media
import fresh_tomatoes

padmavat = media.Movie("Padmavat",
                       "Story of Rani Padmavati Queen of Chittorgarh.",
                       "https://m.media-amazon.com/images/M/MV5BOWZjMjkwM2QtZTJiMy00MmI5LWI2YjEtMmY5NjNiYTE2NTBiXkEyXkFqcGdeQXVyNjQ2MjQ5NzM@._V1_QL50_SY1000_CR0,0,692,1000_AL_.jpg",
                       "https://www.youtube.com/watch?v=X_5_BLt76c0")

sanju = media.Movie("Sanju",
                    "Sanju is a biopic of the controversial life of actor Sanjay Dutt",
                    "https://m.media-amazon.com/images/M/MV5BMjI3NTM1NzMyNF5BMl5BanBnXkFtZTgwOTE4NTgzNTM@._V1_QL50_SY1000_CR0,0,719,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=1J76wN0TPI4")

race3 = media.Movie("Race 3",
                    "Race 3 is a 2018 Indian action thriller film directed by Remo D'Souza and produced under Tips Films and Salman Khan Films.",
                    "https://m.media-amazon.com/images/M/MV5BMzQ4ZTc5ZTItYWRhNi00YTJjLWI4NGMtNjA0ODQ1ZDQxNzkyXkEyXkFqcGdeQXVyNjc4NjAxMzM@._V1_QL50_SY1000_SX750_AL_.jpg",
                    "https://www.youtube.com/watch?v=xBht9TG7ySw")

insideout = media.Movie("Inside Out",
                        "Animated film set in the mind of an adolescent girl",
                        "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",
                        "https://www.youtube.com/watch?v=yRUAzGQ3nSY")

mad_max_fury_road = media.Movie("Mad Max: Fury Road",
                                "The fourth Mad Max film",
                                "https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg",
                                "https://www.youtube.com/watch?v=hEJnMQG9ev8")

socialnetwork = media.Movie("Social Network",
                            "Story of making of the Facebook.",
                            "https://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg",
                            "https://www.youtube.com/watch?v=lB95KLmpLR4&t=65s")

dangal = media.Movie("Dangal",
                     "Former wrestler Mahavir Singh Phogat and his two wrestler daughters struggle towards glory at the Commonwealth Games in the face of societal oppression.",
                     "https://m.media-amazon.com/images/M/MV5BMTQ4MzQzMzM2Nl5BMl5BanBnXkFtZTgwMTQ1NzU3MDI@._V1_QL50_SY1000_CR0,0,713,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=x_7YlGv9u1g")

bossbaby = media.Movie("Boss Baby",
                       "A suit-wearing, briefcase-carrying baby pairs up with his 7-year old brother to stop the dastardly plot of the CEO of Puppy Co.",
                       "https://m.media-amazon.com/images/M/MV5BMTg5MzUxNzgxNV5BMl5BanBnXkFtZTgwMTM2NzQ3MjI@._V1_QL50_SY1000_CR0,0,685,1000_AL_.jpg",
                       "https://www.youtube.com/watch?v=r8kE7rSzfQs")

missionimpossible = media.Movie("Mission:Impossible-Fallout",
                                "Ethan Hunt and his IMF team, along with some familiar allies, race against time after a mission gone wrong.",
                                "https://m.media-amazon.com/images/M/MV5BMTk3NDY5MTU0NV5BMl5BanBnXkFtZTgwNDI3MDE1NTM@._V1_QL50_SY1000_CR0,0,679,1000_AL_.jpg",
                                "https://www.youtube.com/watch?v=wb49-oV0F78")

avengers = media.Movie("Avengers: Infinity War",
                       "The Avengers and their allies must be willing to sacrifice all in an attempt to defeat the powerful Thanos before his blitz of devastation and ruin puts an end to the universe.",
                       "https://m.media-amazon.com/images/M/MV5BMjMxNjY2MDU1OV5BMl5BanBnXkFtZTgwNzY1MTUwNTM@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg",
                       "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

movies = [sanju,padmavat, race3, insideout, mad_max_fury_road, socialnetwork,dangal,bossbaby,missionimpossible,avengers]
fresh_tomatoes.open_movies_page(movies)


