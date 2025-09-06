from django.db import models
from apps.common.models import BaseModel



class Language(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    


class Genre(BaseModel):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Country(BaseModel):
    name = models.CharField(max_length=200)




class Movie(BaseModel):
    movie_genre = models.ManyToManyField("Genre",related_name="movies")
    title = models.CharField(max_length=200)
    country = models.ForeignKey(Country,on_delete=models.PROTECT)
    description = models.TextField(null=True,blank=True)
    age_restriction = models.PositiveSmallIntegerField(default=0)
    year = models.DateField()

    def __str__(self):
        return self.title

class MovieAudio(BaseModel):
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,blank=True, null=True )
    def __str__(self):
        return f"{self.movie.title} ({self.language} audio)"

class MovieSubtitle(BaseModel):
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.movie.title} ({self.language} subtitle)"



class Posterlmage(BaseModel):
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="movies/posters/")
    def __str__(self):
        return f"Poster for {self.movie.title} ({self.language})"


class MovieFile(BaseModel):
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    file = models.FileField(upload_to="movies/videos")
    def __str__(self):
        return f"File: {self.movie.title} ({self.language})"