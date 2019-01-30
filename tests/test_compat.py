import pytest

try:
    import OpenSSL
except ImportError:
    OPENSSL_AVAILABLE = False
else:
    OPENSSL_AVAILABLE = True

@pytest.mark.skipif(OPENSSL_AVAILABLE,
                reason="Requires OpenSSL to be missing to test fallback")
def test_pyopensslcontext_is_none_when_package_missing():
    import requests_toolbelt._compat
    assert requests_toolbelt._compat.PyOpenSSLContext is None
