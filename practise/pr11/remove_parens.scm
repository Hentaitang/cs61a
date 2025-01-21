;;; > (remove-parens '(((1) 2 3) 4 5 (6 (7)) (8 10)))
;;; (1 2 3 4 5 6 7 8 10)
;;; > (remove-parens '(((a) b (c) ()) (d) e (f (((g)))) (h i)))
;;; (a b c d e f g h i)
(define (remove-parens s)
  (cond
    ( (null? s) nil )
    ( (list? (car s)) (append (remove-parens (car s)) (remove-parens (cdr s))))
    ( else (cons (car s) (remove-parens (cdr s))))))

(remove-parens '(((1) 2 3) 4 5 (6 (7)) (8 10)))