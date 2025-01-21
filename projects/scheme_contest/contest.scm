;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: <Your title here>
;;;
;;; Description:
;;;   <It's your masterpiece.
;;;    Use these three lines to describe
;;;    its inner meaning.>

(define (draw)
  ; YOUR CODE HERE
  (repeat 5 (lambda () (fd 100) (repeat 5 drawstar) (rt 144)))
  (exitonclick))

(define (repeat k fn) (if (> k 0) (begin (fn) (repeat (- k 1) fn))))
(define drawstar (lambda () (fd 20) (rt 144)))

; Please leave this last line alone. You may add additional procedures above
; this line.
(draw)