from typing import Annotated

from jsoncanon.util import JSON_Dict
import pytest


@pytest.fixture
def seqcol_level_0() -> Annotated[str, pytest.fixture]:
    return 'wqet7IWbw2j2lmGuoKCaFlYS_R7szczz'


@pytest.fixture
def seqcol_level_1() -> Annotated[JSON_Dict, pytest.fixture]:
    return {
        'lengths': 'IOlarejnLTmdv3-CqehLpcxAR9yNeR1i',
        'names': 'g04lKdxiYtG3dOGeUC5AdKEifw65G0Wp',
        'sequences': 'ixJdEJlNBgz5U49vfIUqmq3kD4oOtLpd'
    }


@pytest.fixture
def seqcol_level_2() -> Annotated[JSON_Dict, pytest.fixture]:
    return {
        'lengths': [248956422, 133797422, 135086622],
        'names': ['chr1', 'chr2', 'chr3'],
        'sequences': [
            'SQ.2648ae1bacce4ec4b6cf337dcae37816',
            'SQ.907112d17fcb73bcab1ed1c72b97ce68',
            'SQ.1511375dc2dd1b633af8cf439ae90cec'
        ]
    }
