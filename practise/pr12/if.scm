(define-macro (if predicate consequent alternative)
  `(or (and ,predicate ,consequent) (and (not ,predicate) ,alternative))
)
; scm> (if #t 1 (/ 1 0))
; 1
; scm> (if #f 1 (/ 1 0))
; Error