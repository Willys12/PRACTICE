#!/usr/bin/env python3
print('we are the {} {}'.format(2025, 'champions!'))

# seperator
print('\n------------------------SEPARATOR------------------------\n')

# keyword arguments
print('This {team} is so {adjective}'.format(team='Arsenal team', adjective='shambolic'))

# seperator
print('\n------------------------SEPARATOR------------------------\n')

# postional and keyword arguments
table = {'Jane': 237890, 'Wilson': 345780, 'Karl': 109992, 'Marriot': 897643}
print('Karl: {0[Karl]:d}; Jane: {0[Jane]:d}; Wilson: {0[Wilson]:d}; '
      'Marriot: {0[Marriot]:d}'.format(table))