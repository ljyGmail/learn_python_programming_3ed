#############################
# Data types
#############################

#############################
# ## Dates and times
#############################

#############################
# ### The standard library
#############################
from enum import Enum
from collections import ChainMap
from collections import defaultdict
from collections import namedtuple
import arrow
from datetime import date, datetime, timedelta, timezone
import time
import calendar as cal
from zoneinfo import ZoneInfo

# date
today = date.today()
print(f'today: {today}')
print(f'today.ctime(): {today.ctime()}')
print(f'today.isoformat(): {today.isoformat()}')
print(f'today.weekday(): {today.weekday()}')
print(f'cal.day_name[today.weekday()]: {cal.day_name[today.weekday()]}')
print(
    f'today.day, today.month, today.year: {today.day, today.month, today.year}')
print(f'today.timetuple(): {today.timetuple()}')

# time
print(f'time.ctime(): {time.ctime()}')
print(f'time.daylight: {time.daylight}')
print(f'time.gmtime(): {time.gmtime()}')
print(f'time.gmtime(0): {time.gmtime(0)}')
print(f'time.localtime(): {time.localtime()}')
print(f'time.time(): {time.time()}')

# datetime
now = datetime.now()
utcnow = datetime.utcnow()
print(f'now: {now}')
print(f'utcnow: {utcnow}')
print(f'now.date(): {now.date()}')
print(f'now.day, now.month, now.year: {now.day, now.month, now.year}')
print(f'now.date() == date.today(): {now.date() == date.today()}')
print(f'now.time(): {now.time()}')
print(
    f'now.hour, now.minute, now.second, now.microsecond: {now.hour, now.minute, now.second, now.microsecond}')
print(f'now.ctime(): {now.ctime()}')
print(f'now.isoformat(): {now.isoformat()}')
print(f'now.timetuple(): {now.timetuple()}')
print(f'now.tzinfo: {now.tzinfo}')
print(f'utcnow.tzinfo: {utcnow.tzinfo}')
print(f'now.weekday(): {now.weekday()}')

# duration
f_bday = datetime(1975, 12, 29, 12, 50, tzinfo=ZoneInfo('Europe/Rome'))
h_bday = datetime(1981, 10, 7, 15, 30, 50, tzinfo=timezone(timedelta(hours=2)))
diff = h_bday - f_bday
print(f'type(diff): {type(diff)}')
print(f'diff.days: {diff.days}')
print(f'diff.total_seconds(): {diff.total_seconds()}')
print(f'today + timedelta(days=49): {today + timedelta(days=49)}')
print(f'now + timedelta(weeks=7): {now + timedelta(weeks=7)}')

# parsing
print(
    f"datetime.fromisoformat('1977-11-24T19:30:13+01:00'): {datetime.fromisoformat('1977-11-24T19:30:13+01:00')}")
print(
    f'datetime.fromtimestamp(time.time()): {datetime.fromtimestamp(time.time())}')

#############################
# ### Third-party libraries
#############################
print(f'arrow.utcnow(): {arrow.utcnow()}')
print(f'arrow.now(): {arrow.now()}')

local = arrow.now('Europe/Rome')
print(f'local: {local}')
print(f"local.to('utc'): {local.to('utc')}")
print(f"local.to('Europe/Moscow'): {local.to('Europe/Moscow')}")
print(f"local.to('Asia/Tokyo'): {local.to('Asia/Tokyo')}")
print(f'local.datetime: {local.datetime}')
print(f'local.isoformat(): {local.isoformat()}')

#############################
# ## The collections module
#############################

#############################
# ### namedtuple
#############################
vision = (9.5, 8.8)
print(f'vision: {vision}')
print(f'vision[0]: {vision[0]}')  # left eye (implicit positional reference)
print(f'vision[1]: {vision[1]}')  # right eye (implicit positional reference)

Vision = namedtuple('Vision', ['left', 'right'])
vision = Vision(9.5, 8.8)
print(f'vision[0]: {vision[0]}')
print(f'vision.left: {vision.left}')  # same as vision[0], but explicit
print(f'vision.right: {vision.right}')  # same as vision[1], but explicit

Vision = namedtuple('Vision', ['left', 'combined', 'right'])
vision = Vision(9.5, 9.2, 8.8)
print(f'vision.left: {vision.left}')  # still correct
# still correct (though now is vision[2])
print(f'vision.right: {vision.right}')
print(f'vision.combined: {vision.combined}')  # the new vision[1]

#############################
# ### defaultdict
#############################
d = {}
d['age'] = d.get('age', 0) + 1  # age not there, we get 0 + 1
print(f'd: {d}')
d = {'age': 39}
d['age'] = d.get('age', 0) + 1  # age is there, we get 40
print(f'd: {d}')

dd = defaultdict(int)  # int is the default type (0 the value)
dd['age'] += 1
print(f'dd: {dd}')

#############################
# ### ChainMap
#############################
default_connection = {'host': 'localhost', 'port': 4567}
connection = {'port': 5678}
conn = ChainMap(connection, default_connection)  # map creation
print(f"conn['port']: {conn['port']}")  # port is found in the first dictionary
# host is fetched from the second dictionary
print(f"conn['host']: {conn['host']}")
print(f'conn.maps: {conn.maps}')
conn['host'] = 'packtpub.com'
print(f'conn.maps: {conn.maps}')
del conn['port']  # let's remove the port information
print(f'conn.maps: {conn.maps}')
# now port is fetched from the second dictionary
print(f"conn['port']: {conn['port']}")
# easy to merge and convert to regular dictionary
print(f'dict(conn): {dict(conn)}')

#############################
# ## Enums
#############################
GREEN = 1
YELLOW = 2
RED = 4
TRAFFIC_LIGHTS = (GREEN, YELLOW, RED)
traffic_lights = {'GREEN': 1, 'YELLOW': 2, 'RED': 4}  # or with a dict


class TrafficLight(Enum):
    GREEN = 1
    YELLOW = 2
    RED = 4


print(f'TrafficLight.GREEN: {TrafficLight.GREEN}')
print(f'TrafficLight.GREEN.name: {TrafficLight.GREEN.name}')
print(f'TrafficLight.GREEN.value: {TrafficLight.GREEN.value}')
print(f'TrafficLight(1): {TrafficLight(1)}')
print(f'TrafficLight(4): {TrafficLight(4)}')
