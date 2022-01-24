niners = [8, 9, 70, 89, 100]

def reverse(niners):
    if len(niners) == 0:
        return niners
    return (
        [niners[-1]]
        + reverse(niners[:len(niners)-1])
    )

my_tuple = ((1,2))
my_tuple += (3, 4)
print(my_tuple)