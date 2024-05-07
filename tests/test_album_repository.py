from lib.album_repository import AlbumRepository

def test_get_all_records(db_connection):
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection)
    albums = repository.all()
    assert len(albums) == 12
    assert albums[0].id == 1