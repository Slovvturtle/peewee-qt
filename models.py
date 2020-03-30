from peewee import *
from datetime import date, time

db = SqliteDatabase('cinema.db')

class BaseModel(Model):
    class Meta:
        database = db

class Director(BaseModel):
    name = CharField(default='John')
    age = IntegerField(default=30)

class Studio(BaseModel):
	title = CharField()
	budget = IntegerField()

class Session(BaseModel):
	date = DateField(default=date.today)
	time = TimeField(default=time(16, 00))
	duration = IntegerField()

class Film(BaseModel):
	title = CharField()
	genre = CharField()
	studio = ForeignKeyField(Studio, backref='films')
	session = ForeignKeyField(Session, backref='film', unique=True)

class Viewer(BaseModel):
	name = CharField()

class Cinema(BaseModel):
	title = CharField()
	address = CharField()

class ViewerToSession(BaseModel):
    viewer = ForeignKeyField(Viewer, backref='viewer_sessions')
    session = ForeignKeyField(Session, backref='session_viewers')

    class Meta:
        primary_key = CompositeKey('viewer', 'session')

class CinemaToFilm(BaseModel):
    cinema = ForeignKeyField(Cinema, backref='cinema_films')
    film = ForeignKeyField(Film, backref='film_cinema')

    class Meta:
        primary_key = CompositeKey('cinema', 'film')

if __name__ == '__main__':
	Director.create_table()
	Film.create_table()
	Studio.create_table()
	Session.create_table()
	Viewer.create_table()
	Cinema.create_table()
	ViewerToSession.create_table()
	CinemaToFilm.create_table()
		

