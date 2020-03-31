from peewee import *
from datetime import date, time
from models import Director, Studio, Session, Film, Viewer, Cinema, ViewerToSession, CinemaToFilm
import peewee


def add_director(name, age):
    return Director.create(name = name, age = age)


def add_studio(title, budget):
    return Studio.create(title = title, budget = budget)


def add_session(date, time, duration):
    return Session.create(date = date, time = time, duration = duration)


def add_film(title, genre, studio, session, director):
    return Director.create(title = title, genre = genre , studio = studio, session = session, director = director)


def add_viewer(name):
    return Studio.create(name = name)


def add_cinema(title, address):
    return Studio.create(title = title, address = address)


if __name__ == '__main__':
    # OPO_GS= Session.create(date = date(2019, 1, 10) , time = time(12, 35), duration = 2)
    #  director = add_director(name = 'Peter Farrelly', age = 63)
    #  studio = add_studio(title = 'Universal Pictures', budget= 23000000)
    #  session = add_session(date = date(2019,1,24), time = time(15,45), duration = 2)
    #  film = add_film(title='Green Book', genre=' biographical comedy-drama', studio= studio.title, session= session.time, director= director.name)
    viewer = add_viewer(name = 'Peter Johnson')
    cinema = add_cinema(title= 'Cinema Village', address = '22 E 12th St, New York')
