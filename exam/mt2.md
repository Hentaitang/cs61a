40.0/45.0

1.  (a) 0
    (b) [4, 5, 2]
    (c) [9, 7, 6]
    (d) [9, 0, 5, 10]
    (e) 4

2.  (a) [[1], [3, 4], [3]]
    (b) [1]
    (c) linear

3.  (a) 1
    (b) b.copies(s)
    (c) lambda s: self.branches[k].inventory.append(s)

4.  (a)
    i.    s == 0
    ii.   n % d == 0
    iii.  s - d
    iv.   f(s, d + 1)

    (b)
    i.    n == s[0]
    ii.   subsums(s[1:], n - s[0])
    iii.  s[:1] + t
    iv:   subsums(s[1:], n)

    (c)
    i.    subsums
    ii.   n % k == 0
    iii.  n
    iv.   lambda k: n % k == 0, range(1, n)

5.  (a)
    i.    a is Link.empty
    ii.   t
    iii.  a, b = a.rest, b.rest
    iv.   s

    (b)
    i.    longest(s.rest, n)
    ii.   s.first <= n
    iii.  Link(s.first, longest(s.rest, n - s.first))

6.  g(x + max_path(b, lambda n: g(x + n)))
