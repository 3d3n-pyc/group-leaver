from datetime import datetime
import pytz

class levels:
    info = '\x1b[34;1mINFO    '
    warning = '\x1b[33;1mWARNING '
    error = '\x1b[31mERROR   '
    critical = '\x1b[41mCRITICAL'


def write(module, message, level):
    date = datetime.now(tz=pytz.timezone('Europe/Paris')).strftime('%Y-%m-%d %H:%M:%S')
    print(f'\x1b[30;1m{date} \x1b[0m{level} \x1b[0m\x1b[35m{module} \x1b[0m{message}')