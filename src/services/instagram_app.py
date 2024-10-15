from typing import Optional

from src.database import Session
from src.models.follower import Follower
from src.parser.inst_parser import InstagramParser


class InstagramApp:
    def __init__(self):
        """Инициализирует приложение InstagramApp с экземпляром InstagramParser."""

        self.parser: InstagramParser = InstagramParser()

    def run(self, profile_name: str, login_username: Optional[str] = None,
            login_password: Optional[str] = None, max_followers: int = 100) -> None:
        """
        Запускает процесс парсинга подписчиков для указанного профиля
        и сохраняет данные в базу данных.
        """

        if login_username and login_password:
            self.parser.login(login_username, login_password)

        with Session() as session:
            for follower in self.parser.get_followers_data(profile_name, max_followers):
                self.add_follower(session, follower)

            session.commit()

        print(f"Данные о {max_followers} подписчиках сохранены в базе данных.")

    @staticmethod
    def add_follower(session: Session, follower_data: dict[str, str | int]) -> None:
        """
        Добавляет данные о подписчике в сессию базы данных.
        """

        follower = Follower(
            username=follower_data.get('username'),
            posts=follower_data.get('posts'),
            followers=follower_data.get('followers'),
            following=follower_data.get('following'),
        )
        session.add(follower)
