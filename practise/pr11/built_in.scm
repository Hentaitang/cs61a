(define count (list 1 2 3 4))
count

(define beats (map (lambda (n) (list 'and 'a n)) count))
beats

(define rhythm (apply append beats))
rhythm