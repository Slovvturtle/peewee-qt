from peewee import *
from datetime import date, time
from models import Director, Studio, Session, Film, Viewer, Cinema, ViewerToSession, CinemaToFilm
import peewee


def add_director(name, age):
    return Director.create(name=name, age=age)


def add_studio(title, budget):
    return Studio.create(title=title, budget=budget)


def add_session(date, time, duration):
    return Session.create(date=date, time=time, duration=duration)


def add_film(title, genre, studio, session, director):
    return Film.create(title=title, genre=genre, studio=studio, session=session, director=director)


def add_viewer(name):
    return Viewer.create(name=name)


def add_cinema(title, address):
    return Cinema.create(title=title, address=address)


def add_view_sess(viewer, session):
    return ViewerToSession.create(viewer=viewer, session=session)


def add_c_film(cinema, film):
    return CinemaToFilm.create(cinema=cinema, film=film)


i = 0
if __name__ == '__main__':
    # director1 = add_director(name='Peter Farrelly', age=63)
    # studio1 = add_studio(title='Universal Pictures', budget=23000000)
    # session1 = add_session(date=date(2019, 1, 24), time=time(15, 45), duration=2)
    # film1 = add_film(title='Green Book', genre='biographical comedy-drama', studio=studio1 , session=session1, director=director1)
    # viewer1 = add_viewer(name='Peter Johnson')
    # cinema1 = add_cinema(title='Cinema Village', address='22 E 12th St, New York')
    # view_sess1 = add_view_sess(viewer=viewer1, session=session1)
    # cin_film1 = add_c_film(cinema=cinema1, film=film1)
    # director2 = add_director(name= 'Guy Ritchie', age=51)
    # studio2 = add_studio(title= 'Miramax', budget=22000000)
    # session2 = add_session(date=date(2020, 2, 13), time= time(18, 30), duration=2)
    # film2 = add_film(title='The Gentlemen', genre='action&comedy', studio= studio2 , session= session2, director=director2)
    # viewer2 = add_viewer(name = 'Jason Smith')
    # cinema2 = add_cinema(title= 'BFI IMAX', address = '1 Charlie Chaplin Walk, South Bank, London')
    # view_sess2 = add_view_sess(viewer=viewer2, session=session2)
    # cin_film2 = add_c_film(cinema=cinema2, film=film2)
    # director3 = add_director(name='Todd Phillips', age=49)
    # studio3 = add_studio(title='Warner Bros. Pictures', budget=62500000)
    # session3 = add_session(date=date(2019, 10, 4), time=time(17, 20), duration=2)
    # film3 = add_film(title='Joker', genre='psychological thriller', studio=studio3, session=session3, director=director3)
    # viewer3 = add_viewer(name='Waene Wilslow')
    # cinema3 = add_cinema(title='Karo-Premier', address=' 24, New Arbat, Moscow')
    # view_sess3 = add_view_sess(viewer=viewer3, session=session3)
    # cin_film3 = add_c_film(cinema=cinema3, film=film3)
    director4 = add_director(name='Tim Miller', age=55)
    studio4 = add_studio(title='20th Century Fox', budget=58000000)
    session4 = add_session(date=date(2016, 2, 8), time=time(21, 50), duration=1)
    film4 = add_film(title='Deadpool', genre='action&comedy', studio=studio4, session=session4,director=director4)
    viewer4 = add_viewer(name='T.J. Kampor')
    cinema4 = add_cinema(title='Quad Cinema', address='34 W 13th St, New York')
    view_sess4 = add_view_sess(viewer=viewer4, session=session4)
    cin_film4 = add_c_film(cinema=cinema4, film=film4)