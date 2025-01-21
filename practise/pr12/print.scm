; scm> (define expr '(* 2 (if (> 2 (+ 1 1)) (+ 3 4) (* 5 6))))
; expr
; scm> (eval expr)
; 60
; scm> (print-evals expr)
; * => #[*]
; 2 => 2
; > => #[>]
; 2 => 2
; + => #[+]
; 1 => 1
; 1 => 1
; (+ 1 1) => 2
; (> 2 (+ 1 1)) => #f
; * => #[*]
; 5 => 5
; 6 => 6
; (* 5 6) => 30
; (if (> 2 (+ 1 1)) (+ 3 4) (* 5 6)) => 30
; (* 2 (if (> 2 (+ 1 1)) (+ 3 4) (* 5 6))) => 60

(define (print-evals expr)
  (if (list? expr)
    (if (equal? (car expr) 'if )
      (begin
        (print-evals (car (cdr expr)))
        (if (eval (car (cdr expr)))
          (print-evals (car (cdr (cdr expr))))
          (print-evals (car (cdr (cdr (cdr expr)))))))
      (map print-evals expr))
    (print expr '=> (eval expr))))