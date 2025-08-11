import requests

import json
from global_vars import *


def auth_request(auth_url: str, auth_domen: str, auth_login: str, auth_password: str):
    master_password_id = "crm"
    headers = {
        'accept': '*/*',
        'accept-language': 'ru,en;q=0.9',
        'content-type': 'application/json',
        'origin': auth_domen,
        'priority': 'u=1, i',
        'referer': f'{auth_domen}/?action=login&master_password_id={master_password_id}',
        'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "YaBrowser";v="25.4", "Yowser";v="2.5"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 YaBrowser/25.4.0.0 Safari/537.36',
    }

    # Данные, которые будут отправлены в теле запроса
    data = {
        "login_name": auth_login,
        "password": auth_password,
        "master_password_id": master_password_id
    }

    try:
        result_dict = {"result_status": None, "token": None}
        # Выполняем POST запрос
        response = requests.post(auth_url, headers=headers, json=data)
        json_response = response.json()
        # Проверка ответа
        if response.status_code == 200 and json_response['status'] == 'ok':
            result_dict["result_status"] = json_response["status"]
            if json_response['token'] != None:
                result_dict["token"] = json_response["token"]
            else:
                result_dict["token"] = None
        else:
            result_dict["result_status"] = json_response["status"]
            result_dict["token"] = None
        return result_dict

    except Exception as e:
        result_dict["result_status"] = e
        return result_dict


def get_report33_data(year_id_to: str, year_id_from:str, auth_data: dict) -> dict:
    token = auth_data['token']
    print(token)
    # Заголовки запроса
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru,en;q=0.9',
        'authorization': f'Bearer {token}',
        'content-type': 'application/json',
        'origin': origin_url,
        'priority': 'u=1, i',
        'referer': referer_url_33,
        'sec-ch-ua': '"Chromium";v="136", "YaBrowser";v="25.6", "Not.A/Brand";v="99", "Yowser";v="2.5"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 YaBrowser/25.6.0.0 Safari/537.36'
    }
    print(headers)
    # Полезная нагрузка (payload)
    payload = [
        {
            "action": "crm-people-transition-percentage2",
            "name": "crm-people-transition-percentage2",
            "params": {
                "year_id_to": "e:academic_years:23",
                "year_id_from": "e:academic_years:22",
                "filial_id__in": [],
                "date": "2025-04-30T00:00:00.000Z"
            }
        }
    ]

    # Отправка запроса
    try:
        response = requests.post(
            url,
            headers=headers,
            json=payload
        )

        # Проверка статуса ответа
        if response.status_code == 200:
            print("Запрос выполнен успешно!")
            print("Ответ сервера:", response.json())
        else:
            print(f"Ошибка при выполнении запроса: {response.status_code}")
            print("Текст ошибки:", response.text)

    except Exception as e:
        print(f"Произошла ошибка при выполнении запроса: {e}")


if __name__ == "__main__":
    auth_data = auth_request(auth_url, auth_domen, login, password)
    report33_data = get_report33_data("e:academic_years:23", "e:academic_years:22", auth_data)

