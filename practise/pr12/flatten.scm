; scm> (* 1 2 (* 3 (* 4)) (+ 5 (* 6 (* 7 8))))
; 8184
; scm> (flatten-nested-* '(* 1 2 (* 3 (* 4)) (+ 5 (* 6 (* 7 8)))))
; (* 1 2 3 4 (+ 5 (* 6 7 8)))
; scm> (* 1 2 3 4 (+ 5 (* 6 7 8)))
; 8184
; scm> (eval (flatten-nested-* '(* 1 2 (* 3 (* 4)) (+ 5 (* 6 (* 7 8))))))
; 8184

(define (is-*-call expr) (and (list? expr) (equal? '* (car expr)))) ; E.g., (* 3 4)
(define (flatten-nested-* expr) ; Return an equivalent expression with no nested calls to *
 (if (not (list? expr)) expr
 (let ((expr (map flatten-nested-* expr))) ; Now expr is (* 1 2 (* 3 4) (+ 5 (* 6 7 8)))
 (if (is-*-call expr)
 (apply append (map (lambda (e) (if (is-*-call e) (cdr e) (list e))) expr))
 expr))))