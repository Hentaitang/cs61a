; Return how many cons cells appear in the diagram for a value s.
(define (cons-count s)
  (if (list? s)
    (+ (length s) (apply + (map cons-count s) ))
    0
  )
)