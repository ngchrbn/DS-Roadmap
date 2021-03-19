# Tuple: ordered, immutable , allows duplicate elements

# Tuple unpacking

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.68722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
]

# print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
# fmt = '{:15} | {:9.4f} | {:9.4f}'
# for name, cc, pop, (latitude, longitude) in metro_areas:
#     if longitude <= 0:
#         print(fmt.format(name, latitude, longitude))


# Named tuples

# The collections.namedtuple function is a factory that produces
# subclasses of tuple enhanced with field names and a
# class name -- which helps debugging

# Two parameters are required to create a named tuple:
# a class name and a list of field names, which are given as
# an iterable of strings or as a single space-delimited string.

from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
# print(tokyo)
# print("Tokyo Population:", tokyo.population)
# print("Tokyo Coordinates:", tokyo.coordinates)

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
# _make() allow you to instatiate a named tuple from an iterable.
# Same as City(*delhi_data)

# _asdict() returns a collections.OrderedDict built from the
# named tuple instance.
for key, value in delhi._asdict().items():
    print(key + ':', value)

