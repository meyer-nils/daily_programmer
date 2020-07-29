"""Solution to challenge 385."""


def flip(bits, pos):
    """Flip bits at position pos.

    Parameters
    ----------
    bits : list of bool
        A list of exactly 64 bits (True or False).
    pos : int
        Position of the bit to be flipped (in range 0-63)

    Returns
    -------
    list of bool
        bits with one flipped position

    """
    assert len(bits) == 64
    assert pos < 64
    assert pos >= 0

    bits[pos] = not bits[pos]
    return bits


def prisoner1(S, X):
    """Prisoner 1 decides wich position to flip.

    Parameters
    ----------
    S : list of bool
        Chess board state.
    X : int
        Location of the key.

    Returns
    -------
    int
        flipped position

    """
    assert len(S) == 64
    assert X < 64
    assert X >= 0

    raise NotImplementedError


def prisoner2(T):
    """Prisoner 2 decodes the position of the key.

    Parameters
    ----------
    T : list of bool
        Chess board state.

    Returns
    -------
    int
        key location

    """
    assert len(T) == 64

    raise NotImplementedError
