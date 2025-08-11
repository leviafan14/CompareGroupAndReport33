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


def get_report33_data(year_id_to: str, year_id_from: str, auth_data: dict) -> dict:
    result_dict = {"data": None, "errors": []}
    people_data = []
    token = auth_data['token']
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
    # Полезная нагрузка (payload)
    payload = {
        "actions": [
            {
                "action": "crm-people-transition-percentage2",
                "name": "crm-people-transition-percentage2",
                "params": {
                    "year_id_to": year_id_to,
                    "year_id_from": year_id_from,
                    "filial_id__in": [],
                    "date": "2025-04-30T00:00:00.000Z"
                }
            }
        ]
    }

    # Отправка запроса
    try:
        response = requests.post(
            url,
            headers=headers,
            json=payload
        )

        # Проверка статуса ответа
        if response.status_code == 200:
            json_response = response.json()
            report_data = json_response['crm-people-transition-percentage2']['result']['data']
            for p in report_data:
                people_data.append(p['person_name'])
            result_dict['data'] = people_data

            return result_dict
        else:
            errors = f"Report33. Статус ответа: {response.status_code}\nТекст:{response.text}"
            result_dict['errors'] = errors

            return result_dict
    except Exception as e:
        errors = f"Report33.Произошла ошибка при выполнении запроса: {e}\n{response.text}"
        result_dict['errors'] = errors

        return result_dict


def get_group_journal(auth_data: dict, start_date: str, end_date: str, group_id: str) -> dict:
    result_dict = {"data": None, "errors": []}
    people_data = []
    token = auth_data['token']
    # Заголовки запроса
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru,en;q=0.9',
        'authorization': f'Bearer {token}',
        'content-type': 'application/json',
        'origin': origin_url,
        'priority': 'u=1, i',
        'referer': "https://crm.talisman-online.ru/lms/groups/detail/e:groups:68343/journal",
        'sec-ch-ua': '"Chromium";v="136", "YaBrowser";v="25.6", "Not.A/Brand";v="99", "Yowser";v="2.5"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 YaBrowser/25.6.0.0 Safari/537.36'
    }
    # Полезная нагрузка (payload)
    payload = {
        "actions": [
            {
                "action": "lms_group_schedule",
                "name": "lms_group_schedule",
                "params": {
                    "group_id": group_id,
                    "start_date": start_date,
                    "end_date": end_date

                }
            }
        ]
    }

    # Отправка запроса
    try:
        response = requests.post(
            url,
            headers=headers,
            json=payload
        )

        # Проверка статуса ответа
        if response.status_code == 200:
            json_response = response.json()
            report_data = json_response['lms_group_schedule']['result']['pupils']['group']
            for p in report_data:
                people_data.append(p['name'])
            result_dict['data'] = people_data

            return result_dict
        else:
            errors = f"Группа: {gruop_id}. Статус ответа: {response.status_code}\nТекст:{response.text}"
            result_dict['errors'] = errors

            return result_dict
    except Exception as e:
        errors = f"Произошла ошибка при получении журнала группы{group_id}: {e}\n{response.text}"
        result_dict['errors'] = errors

        return result_dict



if __name__ == "__main__":
    auth_data = auth_request(auth_url, auth_domen, login, password)
    report33_data = get_report33_data("e:academic_years:23", "e:academic_years:22", auth_data)
    group_journal = get_group_journal(auth_data, "2025-08-01","2025-08-31", "e:groups:68343")
    print(group_journal)

