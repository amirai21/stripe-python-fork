# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from ai21 import util
from ai21.api_resources.abstract import CreateableAPIResource
from ai21.api_resources.abstract import ListableAPIResource
from ai21.api_resources.abstract import UpdateableAPIResource
from ai21.api_resources.abstract import custom_method


@custom_method("list_line_items", http_verb="get", http_path="line_items")
class PaymentLink(
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "payment_link"

    def list_line_items(self, idempotency_key=None, **params):
        url = "/v1/payment_links/{payment_link}/line_items".format(
            payment_link=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        resp = self.request("get", url, params, headers)
        stripe_object = util.convert_to_stripe_object(resp)
        stripe_object._retrieve_params = params
        return stripe_object
