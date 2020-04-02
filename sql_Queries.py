from peewee import *
from datetime import date, time
from models import Director, Studio, Session, Film, Viewer, Cinema, ViewerToSession, CinemaToFilm
import peewee

i=0
if __name__ == '__main__':

    #1st query
    for director in Director.select().join(Film).where(Film.genre =='action&comedy'):
        print(director.name)
    #2nd query

    #3rd query