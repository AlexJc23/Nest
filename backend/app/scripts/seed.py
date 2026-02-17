from app.db.database import SessionLocal
from app.models.user import User
from app.core.security import hash_password


USERS_TO_SEED = [
    {
        "email": "admin@example.com",
        "password": "admin123",
        "first_name": "Admin",
        "last_name": "User",
        "role": "admin",
    },
    {
        "email": "test1@example.com",
        "password": "password123",
        "first_name": "Test",
        "last_name": "User1",
        "role": "member",
    },
    {
        "email": "test2@example.com",
        "password": "password123",
        "first_name": "Test",
        "last_name": "User2",
        "role": "member",
    },
]


def seed_users():
    db = SessionLocal()

    try:
        for user_data in USERS_TO_SEED:
            existing = db.query(User).filter(
                User.email == user_data["email"]
            ).first()

            if existing:
                print(f"{user_data['email']} already exists. Skipping.")
                continue

            user = User(
                email=user_data["email"],
                hashed_password=hash_password(user_data["password"]),
                first_name=user_data["first_name"],
                last_name=user_data["last_name"],
                role=user_data["role"],
                is_active=True,
            )

            db.add(user)
            print(f"{user_data['email']} created.")

        db.commit()

    finally:
        db.close()


if __name__ == "__main__":
    seed_users()
