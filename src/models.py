from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()


class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(200), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, it's a security breach
        }


class Post(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    likes: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    repost: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))  # FK → User


class Picture(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    image_url: Mapped[str] = mapped_column(String(250), nullable=False)
    caption: Mapped[str] = mapped_column(String(250))
    date_posted: Mapped[str] = mapped_column(String(50))
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))  # FK → Post


class Comments(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(String(250), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))  # FK → User
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))  # FK → Post


class Follower(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    follower_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"), nullable=False)
    following_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"), nullable=False)
