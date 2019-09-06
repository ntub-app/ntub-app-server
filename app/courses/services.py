from app.crawlers import course_class


def get_class_course_options() -> dict:
    result = {}
    for sys_id, sys_name in course_class.get_systems().items():
        departments = {}
        for dept_id, dept_name in course_class.get_departments(sys_id).items():
            departments[dept_name] = course_class.get_classes(dept_id)
        result[sys_name] = departments
    return result


def get_class_course(class_id: str) -> list:
    return course_class.get_class_course(class_id)
