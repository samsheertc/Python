<<<<<<< HEAD
import itertools

squares = itertools.starmap(pow,[ (1,2), (2,3), (4,5), (5,6)])

print(squares)       #<itertools.starmap object at 0x0000021D397D85B0>

=======
import itertools

squares = itertools.starmap(pow,[ (1,2), (2,3), (4,5), (5,6)])

print(squares)       #<itertools.starmap object at 0x0000021D397D85B0>

>>>>>>> 87e390981e167a40bc02a1c652c87ed108d68f60
print(list(squares)) #[1, 8, 1024, 15625]