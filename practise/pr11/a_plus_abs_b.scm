#lang racket

(define (a_plus_abs_b a b)
  ((if (< b 0) - +) a b)
)
(a_plus_abs_b 2 3)
(a_plus_abs_b 2 -3)
(a_plus_abs_b -1 4)
(a_plus_abs_b -1 -4)