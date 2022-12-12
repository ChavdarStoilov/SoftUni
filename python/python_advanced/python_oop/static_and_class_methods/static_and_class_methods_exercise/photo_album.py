class PhotoAlbum:

    def __init__(self, pages: int):

        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        
        if photos_count // 4 == 0:
            return cls(photos_count)

        return cls(photos_count // 4)


    def add_photo(self, label: str):

        for slot in range(len(self.photos)):

            if len(self.photos[slot]) == 4:
                continue
        
         
            self.photos[slot].append(label)
   
            return f"{label} photo added successfully on page {slot + 1} slot {self.photos[slot].index(label) + 1}"

        return 'No more free slots'

    
    def display(self):
        result = '-----------\n'
        for pages in range(len(self.photos)):
            page = ' '.join(['[]' for _ in range(len(self.photos[pages]))])
            result += f'{page}\n-----------\n'

        return result



album = PhotoAlbum.from_photos_count(2)
print(album.pages)
print(album.photos)
# import unittest

# class TestsPhotoAlbum(unittest.TestCase):
        
#     def test_add_photo_with_no_free_spots(self):
#         album = PhotoAlbum(1)
#         album.add_photo("baby")
#         album.add_photo("first grade")
#         album.add_photo("eight grade")
#         album.add_photo("party with friends")
#         result = album.add_photo("prom")
#         self.assertEqual(result, "No more free slots")
        
#     def test_add_photo_with_free_spots(self):
#         album = PhotoAlbum(1)
#         album.add_photo("baby")
#         album.add_photo("first grade")
#         album.add_photo("eight grade")
#         album.add_photo("party with friends")
#         self.assertEqual(album.photos, [['baby', 'first grade', 'eight grade', 'party with friends']])
        
#     def test_display_with_one_page(self):
#         album = PhotoAlbum(1)
#         album.add_photo("baby")
#         album.add_photo("first grade")
#         album.add_photo("eight grade")
#         album.add_photo("party with friends")
#         result = album.display().strip()
#         self.assertEqual(result, "-----------\n[] [] [] []\n-----------")
        
#     def test_display_with_three_pages(self):
#         album = PhotoAlbum(3)
#         for _ in range(8):
#             album.add_photo("asdf")
#         result = album.display().strip()
#         self.assertEqual(result, "-----------\n[] [] [] []\n-----------\n[] [] [] []\n-----------\n\n-----------")
        

# if __name__ == "__main__":
#     unittest.main()