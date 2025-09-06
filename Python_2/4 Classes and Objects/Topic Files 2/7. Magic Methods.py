

class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def __str__(self):
        return f'{self.title} - {self.director} - {self.year}'

    def __repr__(self):
        return f'Movie(title={self.title!r}, director={self.director!r}, year={self.year!r})'

movie_1 = Movie('The best', "Kopi", 2000)
print(movie_1)
print(repr(movie_1))

