from pprint import pprint

import requests

from config import get_auth
from pages import get_response


def main():
    auth = get_auth()

    payload = {
        'Login1$UserName': auth[0],
        'Login1$Password': auth[1]
    }
    login_url = "http://wiki.mfc63.ru/login.aspx"

    # Отправляем POST-запрос на страницу авторизации
    response = requests.post(login_url, data=payload)


    # base_url = "http://wiki.mfc63.ru/baza.aspx"
    #
    # response = get_response(url=base_url, auth=)
    print(response.status_code)
    pprint(response.__dict__)

if __name__ == "__main__":
    main()