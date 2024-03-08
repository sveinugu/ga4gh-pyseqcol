import base64
import hashlib

from jsoncanon import canonicalize
from jsoncanon.util import JSON


def seqcol_digest(obj: JSON) -> str:
    return sha512t24u_digest(canonicalize(obj))


def sha512t24u_digest(seq: bytes) -> str:
    """ GA4GH digest function """
    offset = 24
    digest = hashlib.sha512(seq).digest()
    tdigest_b64us = base64.urlsafe_b64encode(digest[:offset])
    return tdigest_b64us.decode('ascii')
