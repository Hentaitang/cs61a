from operator import add, sub, mul, truediv

def converter(c, f):
    """Convert Celsius degrees to Fahrenheit and back."""
    u, v, w, x, y = [connector() for _ in range(5)]
    multiplier(c, w, u)
    multiplier(u, v ,x)
    adder(v, y, f)
    constant(w, 9)
    constant(x, 5)
    constant(y, 32)

def adder(a, b, c):
    """constraint a + b = c"""
    return make_ternary_constraint(a, b, c, add, sub, sub)

def multiplier(a, b, c):
    """constraint a * b = c"""
    return make_ternary_constraint(a, b, c, mul, truediv, truediv)

def make_ternary_constraint(a, b, c, ab, ca, cb):
    """constraint ab(a, b)=c, ca(c, a)=b, cb(c, b)=a"""
    def new_value():
        av, bv, cv = [connector['has_val']() for connector in (a, b, c)]
        if av and bv:
            c['set_val'](constraint, ab(a['val'], b['val']))
        elif av and cv:
            b['set_val'](constraint, ca(c['val'], a['val']))
        elif bv and cv:
            a['set_val'](constraint, cb(c['val'], b['val']))
    def forget_value():
        for connector in (a, b, c):
            connector['forget'](constraint)
    constraint = {'new_val': new_value, 'forget': forget_value}
    for connector in (a, b, c):
        connector['connect'](constraint)
    return constraint

def constant(connector, value):
    """constraint that has a constant value"""
    constraint = {}
    connector['set_val'](constraint, value)
    return constraint

def connector(name=None):
    """A connector between constraints"""
    informant = None
    constraints= []
    def set_value(source, value):
        nonlocal informant
        val = connector['val']
        if val is None:
            informant, connector['val'] = source, value
            if name is not None:
                print(name, '=', value)
            inform_all_except(source, 'new_val', constraints)
        else:
            if val != value:
                print('Contradiction detected:', val, 'vs', value)
    def forget_value(source):
        nonlocal informant
        if informant == source:
            informant, connector['val'] = None, None
            if name is not None:
                print(name, 'is forgotten')
            inform_all_except(source, 'forget', constraints)
    connector = {
        'val': None,
        'set_val': set_value,
        'forget': forget_value,
        'has_val': lambda: connector['val'] is not None,
        'connect': lambda c: constraints.append(c),
    }
    return connector

def inform_all_except(source, message, constraints):
    """Inform all constraints except one"""
    for c in constraints:
        if c != source:
            c[message]()


celsius = connector('Celsius')
fahrenheit = connector('Fahrenheit')
converter(celsius, fahrenheit)
# celsius['set_val']('user', 25)
# fahrenheit['set_val']('user', 212)
# celsius['forget']('user')
# fahrenheit['set_val']('user', 212)