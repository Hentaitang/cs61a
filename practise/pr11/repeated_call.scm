;;; Construct a repeated call expression from an operator and a list of operands.
;;;
;;; scm> (repeated-call 'f '(2 3 4))
;;; (((f 2) 3) 4)
;;; scm> (repeated-call '(f 2) '(3 4))
;;; (((f 2) 3) 4)
;;; scm> (repeated-call 'f nil)
;;; f
(define (repeated-call operator operands)
  (if (null? operands)
    operator
    (repeated-call (list operator (car operands)) (cdr operands))))

(repeated-call 'f '(2 3 4))
(repeated-call '(f 2) '(3 4))
(repeated-call 'f nil)