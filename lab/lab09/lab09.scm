(define (over-or-under num1 num2) (
  cond ((< num1 num2) (- 1))
       ((= num1 num2) 0)
       (else 1)
))

(define (make-adder num) (
  lambda (inc) (+ inc num)
))

(define (composed f g) (
  lambda (x) (f (g x))
))

(define (repeat f n)
  (if (= n 1)
    (lambda (x) (f x))
    (composed (repeat f (- n 1)) f)
  )
)

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b)
  (let (
      (min_num (min a b))
      (max_num (max a b))
    )
    (let (
        (mod (modulo max_num min_num))
      )
      (if (zero? mod)
        min_num
        (gcd min_num mod)
      )
    )
  )
)
