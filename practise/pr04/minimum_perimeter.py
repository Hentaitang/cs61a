def divisors(n):
    """Return the number of positive divisors of n, small than n."""
    return [1] + [x for x in range(2, n) if n % x == 0]

def width(area, height):
    assert area % height == 0, "Area must be a multiple of height"
    return area // height

def perimeter(width, height):
    return 2 * (width + height)

def minimum_perimeter(area):
    heights = divisors(area)
    return min([perimeter(width(area, n), n) for n in heights])
