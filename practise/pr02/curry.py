def curry(f):
  def curry1(x):
    def curry2(y):
      return f(x, y)
    return curry2
  return curry1

def reverse(g):
  def f(x, y):
    return g(y, x)
  return f

square = curry(reverse(pow))(2)