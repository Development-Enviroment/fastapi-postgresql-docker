"""Init Data Insert."""

from database import SessionLocal

from app.models.user import UserModel

db = SessionLocal()


def seed():
    """初期データ挿入関数."""
    user_name = ["田中", "渡辺", "鈴木", "伊藤", "山田"]
    user_email = [
        "tanake@example.com",
        "watanabe@example.com",
        "suzuki@example.com",
        "itou@example.com",
        "yamada@example.com"
        ]
    user_names = [UserModel(name=name) for name in user_name]
    user_emails = [UserModel(email=email) for email in user_email]

    db.add(user_names, user_emails)
    db.commit()

    if __name__ == "__main__":
        print("初期データ挿入...")
        seed()
