from peewee import *
from datetime import date, time
from models import Director, Studio, Session, Film, Viewer, Cinema, ViewerToSession, CinemaToFilm

db = SqliteDatabase('cinema.db')

print(Cinema.cinema_films)