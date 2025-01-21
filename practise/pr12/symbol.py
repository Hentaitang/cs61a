def symbol(exp):
    """Given a define expression exp, return the symbol defined.
    >>> def_x = read_line("(define x (+ 2 3))")
    >>> def_f = read_line("(define (f x) (+ x 3))")
    >>> symbol(def_x)
    'x'
    >>> symbol(def_f)
    'f'
    """
    assert exp.first == "define" and exp.rest is not nil and exp.rest.rest is not nil
    signature = exp.rest.first
    if scheme_symbolp(signature):
        return signature
    else:
        return signature.first
