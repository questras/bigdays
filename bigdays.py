import datetime


def str_to_date(date):
    """Takes date in format YYYY-MM-DD."""
    return datetime.datetime.strptime(date, '%Y-%m-%d')

def years_of_timedelta(timedelta_object):
    return timedelta_object.days / 365

def months_of_timedelta(timedelta_object):
    return timedelta_object.days / 30


class Event:
    def __init__(self, date, description, category):
        if isinstance(date, str):
            date = str_to_date(date)
        self.date = date
        assert isinstance(self.date, datetime.datetime)

        self.description = description
        assert isinstance(self.description, str)

        self.category = category
        assert self._is_correct_category(self.category)

    def _is_correct_category(self, category):
        categories = ['past', 'present', 'future']
        return category in categories

    def get_event_info(self):
        if self.category == 'past':
            return self._get_past_event_info()
        elif self.category == 'present':
            return self._get_present_event_info()
        elif self.category == 'future':
            return self._get_future_event_info()

    def _get_base_event_info(self, info_string, date_string, date_string_before=True): 
        timedelta_obj = datetime.datetime.today() - self.date
        days = abs(timedelta_obj.days)
        months = abs(round(months_of_timedelta(timedelta_obj), 2))
        years = abs(round(years_of_timedelta(timedelta_obj), 2))
        
        info = info_string

        if date_string_before:
            info += f'\n{date_string} {days} days'
            info += f'\n{date_string} {months} months'
            info += f'\n{date_string} {years} years'
        else:
            info += f'\n{days} days {date_string}'
            info += f'\n{months} months {date_string}'
            info += f'\n{years} years {date_string}'

        return info

    def _get_past_event_info(self):
        info_string = f'You {self.description}'
        return self._get_base_event_info(info_string, 'ago', False)

    def _get_present_event_info(self):
        info_string = f'You have been {self.description}'
        return self._get_base_event_info(info_string, 'for')

    def _get_future_event_info(self):
        info_string = f'You will {self.description}'
        return self._get_base_event_info(info_string, 'in')


dates = [('2018-01-01', 'did something', 'past'), 
        ('2020-02-20', 'with someone', 'present'),
        ('2022-03-30', 'graduate', 'future')]

for date, event, category in dates:
    ev = Event(date, event, category)
    print(ev.get_event_info())
    print('-'*50)

