;;; Return a list of two lists; the first n elements of s and the rest
;;; scm> (split (list 3 4 5 6 7 8) 3)
;;; ((3 4 5) (6 7 8))
(define (split s n)
  ; The first n elements of s
  (define (prefix s n)
    (if (zero? n) nil (cons (car s) (prefix (cdr s) (- n 1)))))
  ; The elements after the first n
  (define (suffix s n)
    (if (zero? n) s (suffix (cdr s) (- n 1))))
  (list (prefix s n) (suffix s n)))


(define (split2 s n)
  (if (= n 0)
    (list nil s)
    (let ((split-rest (split2 (cdr s) (- n 1))))
      (cons (cons (car s) (car split-rest))
        (cdr split-rest)))))

(split (list 3 4 5 6 7 8) 3)
(split2 (list 3 4 5 6 7 8) 3)