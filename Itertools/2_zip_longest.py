<<<<<<< HEAD
import itertools

data = [100, 200, 300, 400]

daily_data = list(zip(range(10), data))                      #[(0, 100), (1, 200), (2, 300), (3, 400)
daily_data = list(itertools.zip_longest(range(10), data))    #[(0, 100), (1, 200), (2, 300), (3, 400), (4, None), (5, None), (6, None), (7, None), (8, None), (9, None)]


daily_data1 = itertools.zip_longest(itertools.count(), data) #THIS WILL GO END LESS IF WE USE LIST METHOD

print(next(daily_data1)) #(0, 100)
print(next(daily_data1)) #(1, 200)
print(next(daily_data1)) #(2, 300)
print(next(daily_data1)) #(3, 400)
print(next(daily_data1)) #(4, None)
print(next(daily_data1)) #(5, None)
=======
import itertools

data = [100, 200, 300, 400]

daily_data = list(zip(range(10), data))                      #[(0, 100), (1, 200), (2, 300), (3, 400)
daily_data = list(itertools.zip_longest(range(10), data))    #[(0, 100), (1, 200), (2, 300), (3, 400), (4, None), (5, None), (6, None), (7, None), (8, None), (9, None)]


daily_data1 = itertools.zip_longest(itertools.count(), data) #THIS WILL GO END LESS IF WE USE LIST METHOD

print(next(daily_data1)) #(0, 100)
print(next(daily_data1)) #(1, 200)
print(next(daily_data1)) #(2, 300)
print(next(daily_data1)) #(3, 400)
print(next(daily_data1)) #(4, None)
print(next(daily_data1)) #(5, None)
>>>>>>> 87e390981e167a40bc02a1c652c87ed108d68f60
