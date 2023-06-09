from models import db, Pet, connect_db
from app import app


with app.app_context():
    
    db.drop_all()
    db.create_all()

    
    Pet.query.delete()

    # Add pets
    pet1 = Pet(name="Fido", species="dog", photo_url="https://images.pexels.com/photos/1805164/pexels-photo-1805164.jpeg", age=2)
    pet2 = Pet(name="Whiskers", species="cat", photo_url="https://images.pexels.com/photos/126407/pexels-photo-126407.jpeg", age=3, notes="Very friendly")
    pet3 = Pet(name="Spike", species="porcupine", age=5, available=False)
    pet4 = Pet(name="Buddy", species="dog", photo_url="https://images.pexels.com/photos/356378/pexels-photo-356378.jpeg", age=4, notes="Loves playing fetch")
    pet5 = Pet(name="Mittens", species="cat", photo_url="https://images.pexels.com/photos/17767/pexels-photo.jpg", age=1)
    pet6 = Pet(name="Quill", species="porcupine", photo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Porcupine_NPS11952.jpg/800px-Porcupine_NPS11952.jpg?20050511081041", age=3, notes="Don't pet her, she's a bit prickly", available=False)

    
    db.session.add_all([pet1, pet2, pet3, pet4, pet5, pet6])

    
    db.session.commit()
