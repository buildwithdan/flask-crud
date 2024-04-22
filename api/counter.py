from app import app
from models import Counter

# def increment_and_get_counter():
#     # Create a new Counter instance for each visit
#     new_counter = Counter(count=1)
#     db.session.add(new_counter)
    
#     # Commit the new Counter instance to the database
#     db.session.commit()

#     # Query the total count from the database
#     total_count = db.session.query(db.func.sum(Counter.count)).scalar()

#     return total_count