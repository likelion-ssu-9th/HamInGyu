class Movie:
    def setdata(self, title, director):
        self.title = title
        self.director = director
    def info(self):
        print("제목: ", self.title, ", 감독: ", self.director)

a = Movie()
a.setdata("기생충", "봉준호")
a.info()