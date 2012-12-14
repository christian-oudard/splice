from nose.tools import assert_equal

from strain import Strain

def test_splice():
    strain = Strain(
        (
            (
                (),
            ),
        )
    )
    strain.splice([0, 0], [1])
    assert_equal(
        strain.as_tuple(),
        (
            (),
            (),
        )
    )
