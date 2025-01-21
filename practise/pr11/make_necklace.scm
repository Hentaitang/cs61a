(define (make-necklace beads length)
  ; Returns a list where each value is taken from the BEADS list,
  ; repeating the values BEADS until the list has reached
  ; LENGTH. You can assume that LENGTH is greater than or equal to 1,
  ; and that there is at least one bead in BEADS.
  (if (= length 0)
    nil
    (cons (car beads)
          (make-necklace
            (append (cdr beads) (list (car beads)))
            (- length 1)
          )
    )
  )
)
; Doctests
(expect (make-necklace '(~ *) 3) (~ * ~))
(expect (make-necklace '(~ ^) 4) (~ ^ ~ ^))
(expect (make-necklace '(> 0 <) 9) (> 0 < > 0 < > 0 <))