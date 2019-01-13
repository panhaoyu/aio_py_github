import datetime as _datetime


def default_time():
    return _datetime.datetime.fromtimestamp(1)


def time(string):
    return _datetime.datetime.strptime(string, '%Y-%m-%dT%H:%M:%SZ')
