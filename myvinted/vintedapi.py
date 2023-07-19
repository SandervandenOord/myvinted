import requests
import re


class VintedApi:
    cookie: str
    base_url: str = "https://www.vinted.nl/api/v2/"

    def set_cookie(self) -> None:
        """
        Set cookie needed for being able to call  the vinted api.
        You only need the '_vinted_fr_session' part of the cookie.
        """
        url = "https://www.vinted.nl"
        response = requests.get(url)
        full_cookie = response.headers["Set-Cookie"]
        essential_cookie = re.search("(_vinted_fr_session=.*?;)", full_cookie).group(1)
        self.cookie = essential_cookie

    @property
    def headers(self):
        return {
            "host": "www.vinted.nl",
            "cookie": self.cookie,
        }

    def get_languages(self) -> dict:
        """
        Returns json dictionary of available languages.
        """
        url = self.base_url + "languages"
        response = requests.get(url, headers=self.headers)
        return response.json()


def main():
    vinted_api = VintedApi()
    vinted_api.set_cookie()

    languages = vinted_api.get_languages()
    print(languages)


if __name__ == "__main__":
    main()
