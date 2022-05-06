from abc import ABC

class Date(ABC):
    """
    Абстрактный класс Дата.
    Parameters:
        date_str(str): дата в формате строки, разделенная "-"
    Attributes:
        cls.day (str): день
        cls.month (str): месяц
        cls.year (str): год
    """

    @classmethod
    def __init__(cls, date_str: str) -> None:
        cls.date_str = date_str
        cls.day = ''
        cls.month = ''
        cls.year = ''

    @classmethod
    def from_string(cls, date_str: str) -> str:
        cls.date_str = date_str
        date_lst = cls.date_str.split('-')
        cls.day = date_lst[0]
        cls.month = date_lst[1]
        cls.year = date_lst[2]
        return 'День: {}\tМесяц: {}\t	Год: {}\t'.format(cls.day, cls.month, cls.year)

    @classmethod
    def is_date_valid(cls, date_str: str) -> bool:
        cls.date_str = date_str
        date_lst = cls.date_str.split('-')
        cls.day = date_lst[0]
        cls.month = date_lst[1]
        cls.year = date_lst[2]
        if 0 < int(cls.day) <= 31 and 0 < int(cls.month) <= 12 and 0 < int(cls.year) <= 3000:
            return True
        return False


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))

# День: 10	Месяц: 12	Год: 2077
# True
# False