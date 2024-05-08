from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.database_connection import DatabaseConnection

class Application():
  def __init__(self):
    self._connection = DatabaseConnection()
    self._connection.connect()
    self._connection.seed("seeds/music_library.sql")

  def run(self):
    artist_repository = ArtistRepository(self._connection)
    artists = artist_repository.all()
    album_repository = AlbumRepository(self._connection)
    albums = album_repository.all()

    print("Welcome to the music library manager!\n")
    print("What would you like to do?\n 1 - List all albums\n 2 - List all artists\n")
    user_selection = input("Enter your choice: ")
    if user_selection == "1":
        print("\nHere is the list of albums:")
        for album in albums:
            print(f" * {albums.index(album) + 1} — {album.title}")
    elif user_selection == "2":
        print("\nHere is the list of artists:")
        for artist in artists:
            print(f" * {artists.index(artist) + 1} — {artist.name}")

if __name__ == '__main__':
    app = Application()
    app.run()
