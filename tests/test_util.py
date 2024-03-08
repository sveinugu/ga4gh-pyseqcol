from typing import Annotated

from jsoncanon.util import JSON_Dict
from pyseqcol.util import seqcol_digest
import pytest


def test_digest(seqcol_level_0: Annotated[str, pytest.fixture],
                seqcol_level_1: Annotated[JSON_Dict, pytest.fixture],
                seqcol_level_2: Annotated[JSON_Dict, pytest.fixture]):

    assert seqcol_digest(seqcol_level_2['lengths']) == 'IOlarejnLTmdv3-CqehLpcxAR9yNeR1i'
    assert seqcol_digest(seqcol_level_2['names']) == 'g04lKdxiYtG3dOGeUC5AdKEifw65G0Wp'
    assert seqcol_digest(seqcol_level_2['sequences']) == 'ixJdEJlNBgz5U49vfIUqmq3kD4oOtLpd'

    seqcol_level_1 = {
        'lengths': 'IOlarejnLTmdv3-CqehLpcxAR9yNeR1i',
        'names': 'g04lKdxiYtG3dOGeUC5AdKEifw65G0Wp',
        'sequences': 'ixJdEJlNBgz5U49vfIUqmq3kD4oOtLpd'
    }
    assert seqcol_digest(seqcol_level_1) == 'wqet7IWbw2j2lmGuoKCaFlYS_R7szczz'

    assert seqcol_digest({}) == 'J8dGcK23UHX60FjVzq97IMTneGyDuuij'
    assert seqcol_digest([]) == 'slspTLTetp6gCkw88xE5BIAbYBXllWvQ'
    assert seqcol_digest('') == 'ZNJFYJcMoU00m-oOfSUm1HVL8yg1aKtN'
    assert seqcol_digest(True) == 'kSDNX67wegjpcf8CSj_L6h46a0QUKm2C'
    assert seqcol_digest(None) == 'BPj_JoJgSGLkBb-I3hAu13EKxFwSBZV2'

    with pytest.raises(TypeError):
        seqcol_digest(set())  # type: ignore
