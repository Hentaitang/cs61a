#lang racket
(require teachpacks/racket-turtle)

; (define (repeat k fn)
;   (if (> k 0)
;     (begin (fn) (repeat (- k 1) fn))
;     '()
;   )
; )

; (repeat 5 (
;   lambda () (fw 100)
;             (repeat 5 (lambda () (fw 20) (rt 144)))
;             (rt 144)
;   )
; )


; (define star (list (forward 20)
;                     (turn-right 144)))
; (define repeat-star (repeat 5 star))
; (define repeat-big-star (repeat 5 (list (forward 100) (repeat 5 star) (turn-right 144))))
; (draw repeat-big-star)

(define (tri fn) (repeat 3 (list (fn) (turn-left 120))))
(define (sier d k)
  (tri (lambda () (if (= k 1) (forward d) (leg d k))))
)
(define (leg d k)
  (list (sier (/ d 2) (- k 1))
        (pen-up)
        (forward d)
        (pen-down))
)
(draw (sier 400 6))