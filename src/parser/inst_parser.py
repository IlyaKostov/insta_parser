from typing import Generator

import instaloader
from instaloader import Profile


class InstagramParser:
    def __init__(self) -> None:
        """Инициализация класса InstagramParser с экземпляром Instaloader."""

        self.loader: instaloader.Instaloader = instaloader.Instaloader()

    def login(self, username: str, password: str) -> None:
        """Вход в аккаунт Instagram."""

        try:
            self.loader.login(username, password)
        except instaloader.exceptions.ConnectionException as e:
            print(f"Ошибка при подключении: {e}")
        except instaloader.exceptions.LoginException as e:
            print(f"Ошибка при логине: {e}")

    def get_followers_data(self, profile_name: str, max_followers: int) -> Generator[dict[str, int], None, None]:
        """Получение данных о подписчиках указанного профиля."""

        profile: Profile = instaloader.Profile.from_username(self.loader.context, profile_name)
        followers = profile.get_followers()

        for idx, follower in enumerate(followers):
            if idx >= max_followers:
                break

            yield {
                'username': follower.username,
                'posts': follower.mediacount,
                'followers': follower.followers,
                'following': follower.followees
            }
