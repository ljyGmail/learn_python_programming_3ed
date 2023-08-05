#######################################
# The map, zip, and filter functions
#######################################

#############
# ## map
#############
# map.example.py
# 1 iterable, not useful! Let's use list
print(f'map(lambda *a: a, range(3)): {map(lambda *a: a, range(3))}')
print(
    f'list(map(lambda *a: a, range(3))): {list(map(lambda *a: a, range(3)))}')  # 1 iterable
print(
    f"list(map(lambda *a: a, range(3), 'abc')): {list(map(lambda *a: a, range(3), 'abc'))}")  # 2 iterables
print(
    f"list(map(lambda *a: a,range(3), 'abc', range(4,7))): {list(map(lambda *a: a,range(3), 'abc', range(4,7)))}")  # 3 iterables

# map stops at the shortest iterator
print(
    f"list(map(lambda *a: a, (), 'abc')): {list(map(lambda *a: a, (), 'abc'))}")  # empty tuple is shortest
print(
    f"list(map(lambda *a: a, (1, 2), 'abc')): {list(map(lambda *a: a, (1, 2), 'abc'))}")  # (1, 2) shortest
print(
    f"list(map(lambda *a: a, (1, 2, 3, 4), 'abc')): {list(map(lambda *a: a, (1, 2, 3, 4), 'abc'))}")  # 'abc' shortest


# decorate.sort.undecorate.py
students = [
    dict(id=0, credits=dict(math=9, physics=6, history=7)),
    dict(id=1, credits=dict(math=6, physics=7, latin=10)),
    dict(id=2, credits=dict(history=8, physics=9, chemistry=10)),
    dict(id=3, credits=dict(math=5, physics=5, geography=7)),
]


def decorate(student):
    # create a 2-tuple (sum of credits, student) from student dict
    return (sum(student['credits'].values()), student)


def undecorate(decorated_student):
    # discard sum of credits, return original student dict
    return decorated_student[1]


students = sorted(map(decorate, students), reverse=True)
students = list(map(undecorate, students))

print(f'students: {students}')

#############
# ## zip
#############
# zip.grades.py
grades = [18, 23, 30, 27]
avgs = [22, 21, 29, 24]
print(f'list(zip(avgs, grades)): {list(zip(avgs, grades))}')
print(
    f'list(map(lambda *a: a, avgs, grades)): {list(map(lambda *a: a, avgs, grades))}')  # equivalent to zip

# maxims.py
a = [5, 9, 2, 4, 7]
b = [3, 7, 1, 9, 2]
c = [6, 8, 0, 5, 3]
maxs = map(lambda n: max(*n), zip(a, b, c))
print(f'list(maxs): {list(maxs)}')

#############
# ## filter
#############
# filter.py
test = [2, 5, 8, 0, 0, 1, 0]
print(f'list(filter(None, test)): {list(filter(None, test))}')
# equivalent to previous one
print(f'list(filter(lambda x: x, test)): {list(filter(lambda x: x, test))}')
# keep only items > 4
print(
    f'list(filter(lambda x: x > 4, test)): {list(filter(lambda x: x > 4, test))}')
