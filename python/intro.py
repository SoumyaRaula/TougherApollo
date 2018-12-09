from my_module import find_index, test 
import sys
import random
import datetime
import calendar
import antigravity

# sys.path.append("/test/path")

courses = ['History', 'Civics', 'Maths']
random_course = random.choice(courses)

index = find_index(courses, random_course)

print('Chosen String {}'.format(random_course))
print('Index {}'.format(index))
print(datetime.datetime.now())
print(calendar.isleap(2017))
# print(sys.path)