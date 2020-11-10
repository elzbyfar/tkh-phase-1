class Song:
    def __init__(self, title, artist, genre):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.price = 0.99
        self.purchases = 0
        self.total_sales = 0.00
        
    def display_info(self):
        return f"{self.title} by {self.artist}"
    
    def buy(self):
        self.purchases += 1
        self.total_sales += self.price
        return f"Thank you for your purchase of {self.display_info()}."
    
    def more_info(self):
        return f"'{self.title}' is a {self.genre} song. It has been purchased {self.purchases} times. The song has grossed ${'{0:.2f}'.format(self.total_sales)} to date."
    
    def __add__(self, other_song):
        return self.price + other_song.price
                

if __name__ == '__main__':
    import sys
    song_info = sys.argv
    song = Song(*song_info[1:])
    
    print(song.display_info())
    