"""Utility functions related to symmetry groups.

Currently, only a very small set of groups and site counts are supported.
The :func:`group_create` helper returns both the symmetry generators and the
character table associated with the requested configuration.

New groups can be added by extending the conditional table below.  Each new
entry must specify the permutation generators (``sym_gen``) and the
corresponding character table (``char_table``).  In the future, it may be
possible to automatically generate character tables directly from the
generators.
"""


def group_create(Nsites, group):
    """Return symmetry generators and character table for a given group.

    Parameters
    ----------
    Nsites : int
        Number of lattice sites.
    group : str
        Name of the symmetry group (Schönflies notation).

    Returns
    -------
    tuple[list[list[int]], list[list[int]]]
        The symmetry generators and the associated character table.

    Raises
    ------
    ValueError
        If the combination ``(Nsites, group)`` is not supported.
    """

    if Nsites == 2 and group == "c2":
        sym_gen = [[1, 0]]
        char_table = [[1, 1], [1, -1]]
    elif Nsites == 3 and group == "c2":
        sym_gen = [[1, 0, 2]]
        char_table = [[1, 1], [1, -1]]
    elif Nsites == 3 and group == "d3":
        sym_gen = [[1, 0, 2]]
        char_table = [[1, 1, 1], [1, 1, -1], [2, -1, 0]]
    elif Nsites == 4 and group == "c2":
        sym_gen = [[1, 0, 3, 2]]
        char_table = [[1, 1], [1, -1]]
    elif Nsites == 4 and group == "c2v":
        sym_gen = [[3, 2, 1, 0], [1, 0, 3, 2]]
        char_table = [
            [1, 1, 1, 1],
            [1, 1, -1, -1],
            [1, -1, 1, -1],
            [1, -1, -1, 1],
        ]
    else:  # unsupported combination
        raise ValueError(f"Unsupported combination of Nsites={Nsites} and group='{group}'")

    return sym_gen, char_table
