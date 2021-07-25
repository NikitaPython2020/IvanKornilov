from functools import reduce

NewDate = '2001-01-08'
NewValue = 3

stats = {
    '2001-01-01' : 1,
    '2001-01-06' : 2,
    '2001-01-08': 5
}

stats.setdefault('2010-01-08', 0)


if NewDate in stats:
    print(' ok ')

else:
    stats[NewDate] = NewValue

NewStats = stats.copy()

stats['2010-01-08'] = 200

print(stats)
print(NewStats)
