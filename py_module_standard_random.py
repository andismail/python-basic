import random

rng = random.Random()  # Create a black box object that generates random numbers
print(rng)

dice_throw = random.randrange(1, 7)  # Return an int, one of 1,2,3,4,5,6
print(dice_throw)

delay_in_seconds = rng.random() * 5.0
print(delay_in_seconds)

r_odd = rng.randrange(1, 100, 2)
print(r_odd)

# shuffle
cards = list(range(10))
print(cards)
rng.shuffle(cards)
print(cards)


# WARN: duplicate will in the result
def make_random_ints(num, lower_bound, upper_bound):
    """
      Generate a list containing num random ints between lower_bound
      and upper_bound. upper_bound is an open bound.
    """
    rng = random.Random()  # Create a random number generator
    result = []
    for i in range(num):
        result.append(rng.randrange(lower_bound, upper_bound))
        # result.append(random.randrange(lower_bound, upper_bound))
    return result


# But what if you don’t want duplicates? If you wanted 5 distinct months, then this algorithm is wrong.
# In this case a good algorithm is to generate the list of possibilities, shuffle it, and slice off the number of elements you want:
xs = list(range(1, 13))  # Make list 1..12  (there are no duplicates)
rng = random.Random()  # Make a random number generator
rng.shuffle(xs)  # Shuffle the list
result = xs[:5]  # Take the first five elements
print(result)
# In statistics courses, the first case — allowing duplicates — is usually described as pulling balls out of a bag with
# replacement — you put the drawn ball back in each time, so it can occur again. The latter case, with no duplicates,
# is usually described as pulling balls out of the bag without replacement. Once the ball is drawn,
# it doesn’t go back to be drawn again. TV lotto games work like this.
