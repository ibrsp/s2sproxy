import os
from saml2 import BINDING_HTTP_REDIRECT
from saml2 import BINDING_HTTP_POST


def full_path(path):
    return os.path.join(os.path.dirname(__file__), path)


BASE = "http://example.com"

CONFIG = {
    "entityid": "{}/unittest_sp.xml".format(BASE),
    "service": {
        "sp": {
            "endpoints": {
                "assertion_consumer_service": [
                    ("%s/acs/redirect" % BASE, BINDING_HTTP_REDIRECT),
                    ("%s/acs/post" % BASE, BINDING_HTTP_POST)
                ],
            },
            "allow_unsolicited": "true",
        },
    },
    "key_file": full_path("../pki/key.pem"),
    "cert_file": full_path("../pki/cert.pem"),
    "metadata": {
        "local": [full_path("proxy.xml")],
    }
}
