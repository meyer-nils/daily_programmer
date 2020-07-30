"""Solution to challenge 385."""


def flip(bits, pos):
    """Flip a bit at position pos.

    Parameters
    ----------
    bits : list of bool
        A list of exactly 64 bits representing the board.
    pos : int
        Position of the bit to be flipped (in range 0-63)

    Returns
    -------
    list of bool
        Bits with one flipped position

    """
    assert len(bits) == 64
    assert pos < 64
    assert pos >= 0

    bits[pos] = not bits[pos]
    return bits


def decode_board(bits):
    """Decode the board to a 6-bit binary representation.

    Initially, the state is
    0 <=> 000000.

    We iterate over each board position and flip the corresponding bit, if the position
    is associated with a True value.
    1 <=> 000001: Assuming there is a True value, it will flip the state to 1 <=> 000001.
    2 <=> 000010: If True value: 3 <=> 000011, else it stays 000001.
    ...

    This way, the rightmost bit indicates wether there is an even or odd number of True
    values on all fields indexed with a bit at the rightmost position. This would be
    every second field (1, 3, 5 <=> XXXXX1).
    The second rightmost bit indicates wether there is an odd or even number of bits in
    all positions indexed with a bit in the second rightmost position. This would be
    for example (2,3,6,7 <=> XXXX1X).
    ...

    In total, we can precicely encode a 6 bit number with the state of the board, just
    what we need to tell another prisoner the position of the key.

    Parameters
    ----------
    bits : list of bool
        The current state of the board (64 bits)

    Returns
    -------
    list of 6 bools
        Encoded board state.

    """
    state = 0
    for i, bit in enumerate(bits):
        if bit:
            state ^= i

    print("This board encodes position {0} <=> {1:06b}!".format(state, state))
    return state


def prisoner1(S, X):
    """Prisoner 1 decides wich position to flip.

    First of all, prisoner 1 has to decode the current state of the board. Then,
    prisoner 1 applies a bitwise XOR operation on X and the board state. This
    operation yields the 6 bit representation of the postion to be flipped such that
    the new board state encodes the position X.

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

    board = decode_board(S)

    return board ^ X


def prisoner2(T):
    """Prisoner 2 decodes the position of the key.

    Prisoner 2 simply decodes the board to get a 6-bit representation of the encoded
    position.

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

    return decode_board(T)
