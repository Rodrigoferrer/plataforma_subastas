from app.persistance.UserRepository import UserRepository
# from app.persistence.PlaceRepository import PlaceRepository
# from app.persistence.ReviewRepository import ReviewRepository
# from app.persistence.AmenityRepository import AmenityRepository
from app.models.user import User
# from app.models.amenity import Amenity
# from app.models.place import Place
# from app.models.review import Review



class HBnBFacade:
    def __init__(self):
        self.user_repo = UserRepository() #self.user_repo = InMemoryRepository()
        # self.place_repo = PlaceRepository()#self.place_repo = InMemoryRepository()
        # self.review_repo = ReviewRepository()#self.review_repo = InMemoryRepository()
        # self.amenity_repo = AmenityRepository()#self.amenity_repo = InMemoryRepository()
   
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def get_all_users(self):
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        return self.user_repo.update(user_id, user_data)