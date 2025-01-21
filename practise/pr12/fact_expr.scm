; scm> (fact-expr 5)
; (* 5 (* 4 (* 3 (* 2 (* 1 1)))))
(define (fact-expr n)
  (if (= n 0) 1 `(* ,n ,(fact-expr (- n 1)) )))