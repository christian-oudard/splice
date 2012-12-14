from nose.tools import assert_equal, assert_raises

from strain import Strain

def test_splice():
    strain = Strain(
        (
            (
                (),
            ),
        ))
    strain.splice([0, 0], [1])
    assert_equal(
        strain.as_tuple(),
        (
            (),
            (),
        )
    )

    strain = Strain(
        (
            (),
            (),
        )
    )
    strain.splice([0], [1, 0])
    assert_equal(
        strain.as_tuple(),
        (
            (
                (),
            ),
        )
    )

def test_splice_subtree():
    strain = Strain(
        (
            (),
            (
                (),
                (),
            ),
        )
    )
    strain.splice([1], [0, 0])
    assert_equal(
        strain.as_tuple(),
        (
            (
                (
                    (),
                    (),
                ),
            ),
        )
    )

def test_splice_illegal():
    # Try to splice onto a descendant of the source node.
    strain = Strain(
        (
            (
                (),
            ),
        )
    )
    assert_raises(
        ValueError,
        lambda: strain.splice([0], [0, 0])
    )

    # Try to create a node with too many children.
    strain = Strain(
        (
            (),
            (
                (),
            ),
        )
    )
    assert_raises(
        ValueError,
        lambda: strain.splice([1, 0], [0])
    )

def test_is_legal():
    strain = Strain(
        (
            (),
            (),
        )
    )
    assert_equal(strain.is_legal(), True)

    strain = Strain(
        (
            (),
            (),
            (),
        )
    )
    assert_equal(strain.is_legal(), False)

def test_available_spots():
    strain = Strain(
        (
            (),
            (
                (),
            ),
        )
    )
    assert_equal(
        sorted(strain.available_spots()),
        [
            [0, 0],
            [1, 0],
            [1, 0, 0],
            [1, 1],
        ]
    )
