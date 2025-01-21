;;; scm> (even-subsets '(3 4 5 7))
;;; ((5 7) (4 5 7) (4) (3 7) (3 5) (3 4 7) (3 4 5))
(define (subsets-helper f s)
  (append (map (lambda (t) (cons (car s) t))
              (if (f (car s))
                (even-subsets (cdr s))
                (odd-subsets (cdr s))
              )
            )
          (if (f (car s)) (list (list (car s))) nil)
  )
)

(define (even-subsets s)
  (if (null? s) nil
    (append (even-subsets (cdr s))
            (subsets-helper even? s)
  ))
)

(define (odd-subsets s)
  (if (null? s) nil
    (append (odd-subsets (cdr s))
            (subsets-helper odd? s)
  ))
)
(even-subsets '(3 4 5 7))

(define (nonempty-subsets s)
  (if (null? s) nil
    (let ((rest (nonempty-subsets (cdr s))))
      (append rest
              (map (lambda (t) (cons (car s) t)) rest)
              (list (list (car s)))
      )
    )
  )
)

(define (even-subsets2 s)
  (filter (lambda (t) (even? (apply + t))) (nonempty-subsets s))
)

(even-subsets2 '(3 4 5 7))