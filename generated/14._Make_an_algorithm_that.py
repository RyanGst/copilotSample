# Make an algorithm that counts from 1 to 100
# and for every multiple of 10 emits a message: “Multiple of 10”

for i in range(1, 101):
    if i % 10 == 0:
        print('Multiple of 10')