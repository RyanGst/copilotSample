#  Read a 6-element vector A containing the Mega Sena template Next, read a 10-element vector B containing a bet Write down how many points the bettor scored, and whether he scored the sena (6 hits), the corner (5 hits) or the quad (4 hits)

# read the template
template = [int(x) for x in input().split(' ')[:6]]

# read the bet

bet = [int(x) for x in input().split(' ')[:10]]

# count the hits

hits = 0

for number in bet:
    if number in template:
        hits += 1

# print the results

print('Hits: {}'.format(hits))