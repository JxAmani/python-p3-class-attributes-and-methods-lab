class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update class attributes
        Song.count += 1

        if genre not in Song.genres:
            Song.genres.append(genre)

        if artist not in Song.artists:
            Song.artists.append(artist)

        # Update genre count
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

        # Update artist count
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1


# --- Example usage ---
def main():
    song1 = Song("99 Problems", "Jay-Z", "Rap")
    song2 = Song("Halo", "Beyonce", "Pop")
    song3 = Song("Numb", "Linkin Park", "Rock")
    song4 = Song("Encore", "Jay-Z", "Rap")

    # Print all the class-level data
    print("Total songs:", Song.count)
    print("Genres:", Song.genres)
    print("Artists:", Song.artists)
    print("Genre counts:", Song.genre_count)
    print("Artist counts:", Song.artist_count)

    # Access instance data
    print("\nFirst song info:")
    print("Name:", song1.name)
    print("Artist:", song1.artist)
    print("Genre:", song1.genre)

if __name__ == "__main__":
    main()
