import requests

from bs4 import BeautifulSoup

from config.components.crawler import CLASS_COURSE_URL

from util.list import to_dict


TIME_KEYS = ('display_name', 'start_at', 'end_at')
CLASS_KEYS = ('name', 'teacher', 'room')


def parse_options(data: dict) -> dict:
    res = requests.post(CLASS_COURSE_URL, data)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    options = soup.select('option')
    return {o['value']: o.text for o in options if o['value'] != '-1'}


def get_systems() -> dict:
    data = {'flag': '學制'}
    return parse_options(data)


def get_departments(system_id: str) -> dict:
    data = {'strEdu': system_id, 'flag': '學系'}
    return parse_options(data)


def get_classes(department_id: str) -> dict:
    data = {'strDept': department_id, 'flag': '班級'}
    return parse_options(data)


def get_class_course(class_id: str) -> list:
    date = {'strClass': class_id, 'flag': '班級課表查詢'}
    res = requests.post(CLASS_COURSE_URL, date)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    result = []
    for row in soup.select('tbody tr'):
        time = to_dict(TIME_KEYS, row.select_one('th').strings)
        classes = []
        for c in row.select('td'):
            class_data = list(c.strings)
            if len(class_data) > 3:  # Handle multiple teacher (EX. 專題)
                class_data[1] = '、'.join(class_data[1::3])
                class_data = class_data[:3]
            classes.append(to_dict(CLASS_KEYS, class_data))
        result.append({**time, 'classes': classes})
    return result
