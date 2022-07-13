from __future__ import absolute_import, division, print_function

import os

import ai21


ai21.api_key = os.environ.get("STRIPE_SECRET_KEY")

print("Attempting charge...")

proxy = {
    "http": "http://<user>:<pass>@<proxy>:<port>",
    "https": "http://<user>:<pass>@<proxy>:<port>",
}

clients = (
    ai21.http_client.RequestsClient(
        verify_ssl_certs=ai21.verify_ssl_certs, proxy=proxy
    ),
    ai21.http_client.PycurlClient(
        verify_ssl_certs=ai21.verify_ssl_certs, proxy=proxy
    ),
    ai21.http_client.Urllib2Client(
        verify_ssl_certs=ai21.verify_ssl_certs, proxy=proxy
    ),
)

for c in clients:
    ai21.default_http_client = c
    resp = ai21.Charge.create(
        amount=200,
        currency="usd",
        card="tok_visa",
        description="customer@gmail.com",
    )
    print("Success: %s, %r" % (c.name, resp))
