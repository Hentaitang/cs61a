;;; Return a curried version of f that can be called repeatedly num-args times.
;;;
;;; scm> (((((curry 3) +) 4) 5) 6) ; (+ 4 5 6) evaluates to 15
;;; 15
;;; scm> ((curry 0) +) ; (+) evaluates to 0
;;; 0
;;; scm> (((curry 1) +) 3) ; (+ 3) evaluates to 3
;;; 3
;;; scm> (((((curry 3) list) 4) 5) 6) ; (list 4 5 6) evaluates to (4 5 6)
;;; (4 5 6)
(define (curry num-args)
  (lambda (f) (curry-helper num-args (lambda (s) (apply f s)))))
;;; curry-helper's argument g is a one-argument procedure that takes a list.
;;;
;;; scm> ((((curry-helper 3 cdr) 5) 6) 7) ; (cdr '(5 6 7)) => (6 7)
;;; (6 7)
(define (curry-helper num-args g)
  (if (= num-args 0)
    (g nil)
    (lambda (x) (curry-helper (- num-args 1) (lambda (s) (g (cons x s)))))))

((((curry-helper 3 cdr) 5) 6) 7) ; (cdr '(5 6 7)) => (6 7)