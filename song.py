class Song:
    """Class to represent a song
    
    Attributes: 
        title(str): The title of the song.
        artist(Artist): The performer of the song is an Artist object.
        duration (int): The duration of the song. May be zero."""
    
    def __init__(self, title, artist, duration=0):
        """Song init method"""
        self.title = title
        self.artist = artist
        self.duration = duration

class Album:
    """Class to represent album
    Attributes:
        album_name(str): The name of the album.
        year(int): The year the album was released.
        artist(Artist): The artist that performed.
            If not specified, it will default to 'Various Artists'.
        tracks (List[Song]): A list of the songs of the album.
    Methods:
        addSong: Used to add a song to the tracks of the album.
        """
    def __init__(self,album_name, year, artist=None):
        self.album_name = album_name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist
        self.tracks = []
        
    def addSong(self, song, position=None):
        """Adds a song to the tracklist
            args: song(Song): A song to add to the tracklist
            position(int - optional): The number of the track in the tracklist"""
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)
            
class Artist:
    """A basic class to store artist details.
    
    Attributes:
        name(str): Name of the artist.
        albums(List[Album]): List of the albums by artist.
    Methods:
        addAlbum: Used to add a new album to the artist's album List.
        """
    def __init__(self, name):
        self.name = name
        self.albums =[]
    
    def addAlbum(self, album):
        
        """Used to add a new album to the list.
        If the album is already present, it will not be added again."""
        
        self.albums.append(album)
        
        
def load_data():
    new_artist = None
    new_album = None
    artist_list = []
    with open('albums.txt', 'r') as albums:
        for line in albums:
            #data row contains artist album year song
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split("\t"))
            year_field = int(year_field)
            print ("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))
            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist.name != artist_field:
                new_artist.addAlbum(album_field)
                artist_list.append(new_artist)
                new_artist = Artist(artist_field)
                new_album = None
                
            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.album_name != album_field:
                new_artist.addAlbum(new_album)
                new_album = Album(album_field, year_field, new_artist)
            new_song = Song(song_field, new_artist)
            new_album.addSong(new_song)
        #after reading last line of text, we will have an artist and album that haven't been processed yet - process them now
        if new_artist is not None:
            if new_album is not None:
                new_artist.addAlbum(new_album)
            artist_list.append(new_artist)
    return (artist_list)

def create_checkfile(artist_list):
    with open("checkfile.txt", 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.album_name}\t{1.year}\t{2.name}".format(new_artist,new_album,new_song)
                         ,file=checkfile)
if __name__ == "__main__":
    lst = load_data()
    create_checkfile(lst)