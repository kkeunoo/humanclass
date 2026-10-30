class Song:
    def __init__(self, title, singer, album, lyrics):
        self.title = title
        self.singer = singer
        self.album = album
        self.lyrics = lyrics
class Chart:
    def __init__(self):
        self.songs = []
    def add_song(self, song):
        self.songs.append(song)
    def show_songs(self):
        for song in self.songs:
            print(f'{song.title}-{song.singer}')
chart = Chart()
chart.add_song(Song('첫 곡', '가수 A', '앨범 A', '연습 가사 A'))
chart.add_song(Song('둘째 곡', '가수 B', '앨범 B', '연습 가사 B'))
chart.show_songs()
other_chart = Chart()
print('다른 목록', len(other_chart.songs))
class Account:
    def __init__(self):
        self.__address = ''
    def set_address(self, address):
        if address.strip() == '':
            print('주소 확인')
            return
        self.__address = address
    def get_address(self):
        return self.__address
account = Account()
account.set_address('천안')
account.set_address('   ')
print(account.get_address())
class Shop:
    def __init__(self, name, money):
        self.name = name
        self.money = money
shop1 = Shop('천안점', 20000)
shop2 = Shop('아산점', 50000)
print(shop1.name, shop1.money)
print(shop2.name, shop2.money)
