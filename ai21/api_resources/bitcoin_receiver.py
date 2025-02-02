# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from ai21 import util
from ai21.api_resources.abstract import ListableAPIResource
from ai21.api_resources.customer import Customer
from ai21.six.moves.urllib.parse import quote_plus


class BitcoinReceiver(ListableAPIResource):
    OBJECT_NAME = "bitcoin_receiver"

    @classmethod
    def class_url(cls):
        return "/v1/bitcoin/receivers"

    def instance_url(self):
        token = util.utf8(self.id)
        extn = quote_plus(token)

        if hasattr(self, "customer"):
            customer = util.utf8(self.customer)
            base = Customer.class_url()
            cust_extn = quote_plus(customer)
            return "%s/%s/sources/%s" % (base, cust_extn, extn)
        else:
            base = BitcoinReceiver.class_url()
            return "%s/%s" % (base, extn)
