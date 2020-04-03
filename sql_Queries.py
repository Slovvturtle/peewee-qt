from peewee import *
from datetime import date, time
from models import Director, Studio, Session, Film, Viewer, Cinema, ViewerToSession, CinemaToFilm
import peewee

i=0
if __name__ == '__main__':

    #1st query
    for a in Director.select().join(Film).where(Film.genre =='action&comedy'):
        print('Director name is: ',a.name)
    #2nd query
    for a in Cinema.select(Cinema.title,Cinema.address).join(CinemaToFilm).join(Film).where(Film.title == 'Deadpool'):#.order_by(Session.time.desc()):
        print('Cinema title is: ', a.title, '\n', 'Cinema address: ', a.address)
        for b in Session.select(Session.date).join(Film).where(Film.title == 'Deadpool').order_by(Session.time.desc()):
            print('Sessions are: ', b.date)
    #3rd query
    for a in Studio.select(Studio.title, Studio.budget).join(Film).join(Session).join(ViewerToSession).join(Viewer).where(Session.date > date(2016, 2, 8), Viewer.name == 'Waene Wilslow' ):
        print('Studio title is:', a.title, '\n', 'Studio budget is:', a.budget)