from typing import Annotated

from jsoncanon.util import JSON_Dict
from pyseqcol.collection import SequenceCollection
from pyseqcol.exceptions import SeqColNotFoundError, SeqColServiceNotRegisteredError
from pyseqcol.register import get_seqcol_service_register
import pytest
from pytest_httpx import HTTPXMock

#
# def test_get_collection(httpx_mock):
#     case_collection = {
#         'lengths': [248956422, 133797422, 135086622],
#         'names': ['chr1', 'chr2', 'chr3'],
#         'sequences': [
#             'SQ.2648ae1bacce4ec4b6cf337dcae37816',
#             'SQ.907112d17fcb73bcab1ed1c72b97ce68',
#             'SQ.1511375dc2dd1b633af8cf439ae90cec'
#         ]
#     }
#     a = canonicalize(case_collection)
#     print(a)
#     # httpx_mock.add_response()
#
#     # request = httpx_mock.get_request()
#
#
# @pytest.mark.anyio
# async def test_something_async(httpx_mock):
#     loop = asyncio.get_running_loop()
#     loop.set_debug_mode()
#
#     httpx_mock.add_response()
#
#     async with httpx.AsyncClient() as client:
#         response = await client.get('https://test_urlsdf')
#         print(response)


def test_sequence_collection_expand(
    seqcol_level_0: Annotated[str, pytest.fixture],
    seqcol_level_1: Annotated[JSON_Dict, pytest.fixture],
    seqcol_level_2: Annotated[JSON_Dict, pytest.fixture],
    httpx_mock: Annotated[HTTPXMock, pytest.fixture],
):
    seqcol = SequenceCollection(seqcol_level_0)
    assert seqcol.level == 0
    assert seqcol.contents == seqcol_level_0

    with pytest.raises(SeqColServiceNotRegisteredError):
        seqcol.expand(level=1)

    seqColService_1 = 'https://myseqcolservice.somewhere.net'
    seqColService_2 = 'https://seqcolservice.elsewhere.com'

    register = get_seqcol_service_register()
    register.add_seqcol_service(seqColService_1)

    httpx_mock.add_response(url=f'{seqColService_1}/collection/{seqcol_level_0}', status_code=404)
    with pytest.raises(SeqColNotFoundError):
        seqcol.expand()
    assert seqcol.level == 0

    register.add_seqcol_service(seqColService_2)

    httpx_mock.add_response(url=f'{seqColService_1}/collection/{seqcol_level_0}', status_code=404)
    httpx_mock.add_response(
        url=f'{seqColService_2}/collection/{seqcol_level_0}', json=seqcol_level_2)

    seqcol.expand()
    assert seqcol.level == 0
    assert seqcol.contents == seqcol_level_2
