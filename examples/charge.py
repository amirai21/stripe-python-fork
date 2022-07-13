from __future__ import absolute_import, division, print_function

import os

import ai21


ai21.api_key = os.environ.get("STRIPE_SECRET_KEY")

print("Attempting charge...")

resp = ai21.Charge.create(
    amount=200,
    currency="usd",
    card="tok_visa",
    description="customer@gmail.com",
)

print("Success: %r" % (resp))
