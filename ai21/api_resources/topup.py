# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from ai21 import util
from ai21.api_resources.abstract import CreateableAPIResource
from ai21.api_resources.abstract import ListableAPIResource
from ai21.api_resources.abstract import UpdateableAPIResource
from ai21.api_resources.abstract import custom_method


@custom_method("cancel", http_verb="post")
class Topup(CreateableAPIResource, ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME = "topup"

    def cancel(self, idempotency_key=None, **params):
        url = "/v1/topups/{topup}/cancel".format(
            topup=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self
