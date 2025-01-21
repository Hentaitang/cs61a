;;; Take a (possibly nested) call expression s and return
;;; an equivalent expression in which all calls have one argument.
;;;
;;; scm> (one-arg '(abs 3)) ; (abs 3) already takes just 1 argument
;;; (abs 3)
;;;
;;; scm> (+ 4 5 6)
;;; 15
;;; scm> (one-arg '(+ 4 5 6))
;;; (((((curry 3) +) 4) 5) 6)
;;; scm> (eval (one-arg '(+ 4 5 6))) ; Same value as (+ 4 5 6)
;;; 15
;;;
;;; scm> (one-arg '(+ (- 4) (*) (* 5 6)))
;;; (((((curry 3) +) (- 4)) ((curry 0) *)) ((((curry 2) *) 5) 6))
(define (one-arg s)
  (if (number? s) s
    (let ((num-args (- (length s) 1)))
      (if (= num-args 1)
        (list (car s) (one-arg (car (cdr s))))
        (repeated-call (list '(curry num-args) (car s))
          (map one-arg (cdr s))
        )
      )
    )
  )
)