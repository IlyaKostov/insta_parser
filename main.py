from src.config import LOGIN_USERNAME, LOGIN_PASSWORD, PROFILE_NAME
from src.database import engine, Base
from src.services.instagram_app import InstagramApp


def main():
    Base.metadata.create_all(bind=engine)

    app = InstagramApp()
    app.run(PROFILE_NAME, LOGIN_USERNAME, LOGIN_PASSWORD)


if __name__ == '__main__':
    main()
