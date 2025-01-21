; Return a list containing expr n times.
; scm> (repeated-expr 4 '(print 2))
; ((print 2) (print 2) (print 2) (print 2))
(define (repeated-expr n expr)
  (if (zero? n) nil (cons expr (repeated-expr (- n 1) expr)) ))

; Evaluate expr n times and return the last value.
; scm> (repeat (+ 1 2) (print 5))
; 5
; 5
; 5
; scm> (repeat 3 (+ 2 3)) ; (+ 2 3) is evaluated 3 times, but only the last is returned
; 5
(define-macro (repeat n expr)
  (cons 'begin (repeated-expr (eval n) expr)))