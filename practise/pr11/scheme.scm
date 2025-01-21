#lang racket

(+ 1 2)
(+ (* 3 5) (- 10 6))
(>= 2 1)
(if (>= 2 1) 2 1)
(and 1 0 2)
(and 1 (>= 1 2) 2)
(or 1 (>= 1 2) 2)

(define pi 3.14)
(* pi 2)

(define (abs x)
  (if (> x 0) x (- x))
)
(abs 10)
(abs -8)

(define (square x) (* x x))
(square 16)

(define (average x y)
  (/ (+ x y) 2)
)
(average 3 7)

(define (sqrt x)
  (define (good-enough? guess)
    (< (abs (- (square guess) x)) 0.001))
  (define (improve guess)
    (average guess (/ x guess)))
  (define (sqrt-iter guess)
    (if (good-enough? guess)
        guess
        (sqrt-iter (improve guess))))
  (sqrt-iter 1.0)
)
(sqrt 9)

((lambda (x) (+ x 4)) 3)
((lambda (x y z) (+ x y z)) 1 2 3)

(define x (cons 1 2))
x
(car x)
(cdr x)

(cons 1 (cons 2 (cons 3 (cons 4 '()))))
(list 1 2 3 4)
(define one-through-four (list 1 2 3 4))
(car one-through-four)
(cdr one-through-four)
(car(cdr one-through-four))
(cons 10 one-through-four)

(define (length items)
  (if (null? items)
      0
      (+ 1 (length (cdr items)))))

; (define (sqrt x)
;   (define (update guess)
;     (if (= (square guess) x)
;       guess
;       (update (average guess (/ x guess)))))
;   (update 1))
; (sqrt 256)

(define (big_or_not x)
  (cond ((> x 10) (print 'big))
        ((> x 5) (print 'medium))
        (else (print 'small))
  )
)
(big_or_not 15)
(newline)

(define (print_2 x)
  (if (> x 10) (begin (print 'big) (print 'guy))
              (begin (print 'small) (print 'fry)))
)
(print_2 2)