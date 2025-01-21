62.0/75.0

1.  (a) [0, 4, 6, 8]
    (b) [-4, 0, 4]
    (c) [0, 2, 8]

2.  (a) [[3]]
    (b) 4

3.  (a) t > 10
    (b) False
    (c) 10
    (d) 0

4.  (a)
    i.    self.count = 0
    ii.   if self.parent is not None:
    iii.  self.parent.inc()
    iv.   Counter(self)

    (b)
    i.    MissDict.misses.spawn()/Counter(MissDict.misses)
    ii.   result.append(self.d[k])
    iii.  self.misses.inc()
    iv.   {self.misses.count} / {MissDict.misses.count}

5.  (a)
    i.    [s[j]] / s[j:j+1]
    ii.   s[i:j]
    iii.  j+1

    (b)
    i.    s[0] == t[0]
    ii.   promote(s, 0, j)[1:]
    iii.  s[j] == t[0]

    (c)
    i.    promote_link(s.rest, i-1, j-1)
    ii.   insert, tail.first = tail.first, insert
    iii.  s.first
    iv.   s
    v.    <5 7 9 3>

6.  (a)
    i.    n == t.label
    ii.   n % t.label > 0
    iii.  all([products(b, n//t.label) for b in t.branches])

    (b)
    i.    t.label + 1
    ii.   x
    iii.  grow(Tree(k), x // k)
    iv.   not branch.is_leaf() or x == k

7.  (a)
    i.    (f (car s) (car (cdr s)))
    ii.   (cdr s)

    (b)
    i.    cons
    ii.   (list (car s) (car (cdr s)))
    iii.  (cdr s)
    iv.   linear

    (c)
    i.    cons 'and
    ii.   (lambda (p) (append (list proc-name) p))

8.  (a) who, gov
    (b) region=place
    (c) group by job having count(*)=1

9.  (a)  (all-pairs (lambda (x y) (= ,x-expr y)) ,s)