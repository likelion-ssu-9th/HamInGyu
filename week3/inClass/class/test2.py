class Movie:
    def __init__(self, title, director):
        self.title = title
        self.director = director
    def info(self):
        print("제목: ", self.title, ", 감독: ", self.director)

a = Movie("기생충", "봉준호")
a.info()