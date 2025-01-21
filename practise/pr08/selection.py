from link_class import Link


class State:
    electors = {}

    def __init__(self, code, electors):
        self.code = code
        self.electors = electors
        State.electors[code] = electors


battleground = [State("AZ", 11), State("PA", 20), State("NV", 6), State("GA", 16), State("WI", 10), State("MI", 16)]


def print_all(s):
    for x in s:
        print(x)


def wins(states, k):
    """Yield each linked list of two-letter state codes that describes a win by at least k.
    >>> print_all(wins(battleground, 50))
    <AZ PA NV GA WI MI>
    <AZ PA NV GA MI>
    <AZ PA GA WI MI>
    <PA NV GA WI MI>
    >>> print_all(wins(battleground, 75))
    <AZ PA NV GA WI MI>
    """
    if k <= 0 and not states:
        yield Link.empty
    if states:
        first = states[0].electors
        for win in wins(states[1:], k - first):
            yield Link(states[0].code, win)
        yield from wins(states[1:], k + first)


def must_win(states, k):
    """List all states that must be won in every scenario that wins by k.
    >>> must_win(battleground, 50)
    ['PA', 'GA', 'MI']
    >>> must_win(battleground, 75)
    ['AZ', 'PA', 'NV', 'GA', 'WI', 'MI']
    """

    def contains(s, x):
        """Return whether x is a value in linked list s."""
        return (s is not Link.empty) and (s.first == x or contains(s.rest, x))

    return [s.code for s in states if all([contains(w, s.code) for w in wins(states, k)])]


def is_minimal(state_codes, k):
    """Return whether a non-empty list of state_codes describes a minimal win by
    at least k.
    >>> is_minimal(['AZ', 'NV', 'GA', 'WI'], 0) # Every state is necessary
    True
    >>> is_minimal(['AZ', 'GA', 'WI'], 0) # Not a win
    False
    >>> is_minimal(['AZ', 'NV', 'PA', 'WI'], 0) # NV is not necessary
    False
    >>> is_minimal(['AZ', 'PA', 'WI'], 0) # Every state is necessary
    True
    """
    assert state_codes, "state_codes must not be empty"
    votes_in_favor = [State.electors[code] for code in state_codes]
    total_possible_votes = sum(State.electors.values())

    def win_margin(n):
        "Margin of victory if n votes are in favor and the rest are against."
        return n - (total_possible_votes - n)

    if win_margin(sum(votes_in_favor)) < k:
        return False  # Not a win
    in_favor_no_smallest = sum(votes_in_favor) - min(votes_in_favor)
    return win_margin(in_favor_no_smallest) < k
