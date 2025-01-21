(define-macro (switch expr cases)
    `(let ((val ,expr))
        ,(cons
    	    'cond
    	    (map
    	        (lambda (case) (cons
    	           `(equal? val ,(car case))
    		       (cdr case)))
    		    cases))))
