# -*- coding: utf-8 -*-
import media
import movie_page

toy_story = media.Movie("Toy Story",
                        "Woody the cowboy is young Andy’s favorite toy. Yet this changes when Andy get the new super",
                        "https://image.tmdb.org/t/p/original/uMZqKhT4YA6mqo2yczoznv7IDmv.jpg",
                        "https://www.youtube.com/watch?v=K26_sDKnvMU")

#print toy_story.trailer_youtube
doctor_strange = media.Movie("Doctor Strange",
                             "After his career is destroyed, a brilliant but arrogant surgeon gets a new lease on life when a sorcerer takes him under his wing and trains him to defend the world against evil.",
                             "https://image.tmdb.org/t/p/original/xfWac8MTYDxujaxgPVcRD9yZaul.jpg",
                             "https://www.youtube.com/watch?v=HSzx-zryEgM")

finding_dory = media.Movie("Finding Dory",
                           "reunites Dory with friends Nemo and Marlin on a search for answers about her past. What can she remember? Who are her parents? And where did she learn to speak Whale?",
                           "https://image.tmdb.org/t/p/original/iJGNb7X3jQfNHWBkTeRdOsjRvq2.jpg",
                           "https://www.youtube.com/watch?v=NQu-153MnGQ")

movies = [toy_story, doctor_strange, finding_dory]
movie_page.open_movies_page(movies)