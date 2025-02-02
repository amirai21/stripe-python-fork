# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

import ai21
from ai21 import api_requestor
from ai21 import util
from ai21.api_resources.abstract import CreateableAPIResource
from ai21.api_resources.abstract import ListableAPIResource
from ai21.api_resources.abstract import UpdateableAPIResource
from ai21.api_resources.abstract import custom_method
from ai21.six.moves.urllib.parse import quote_plus


@custom_method("accept", http_verb="post")
@custom_method("cancel", http_verb="post")
@custom_method("finalize_quote", http_verb="post", http_path="finalize")
@custom_method(
    "list_computed_upfront_line_items",
    http_verb="get",
    http_path="computed_upfront_line_items",
)
@custom_method("list_line_items", http_verb="get", http_path="line_items")
class Quote(CreateableAPIResource, ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME = "quote"

    def accept(self, idempotency_key=None, **params):
        url = "/v1/quotes/{quote}/accept".format(
            quote=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def cancel(self, idempotency_key=None, **params):
        url = "/v1/quotes/{quote}/cancel".format(
            quote=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def finalize_quote(self, idempotency_key=None, **params):
        url = "/v1/quotes/{quote}/finalize".format(
            quote=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def list_computed_upfront_line_items(self, idempotency_key=None, **params):
        url = "/v1/quotes/{quote}/computed_upfront_line_items".format(
            quote=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        resp = self.request("get", url, params, headers)
        stripe_object = util.convert_to_stripe_object(resp)
        stripe_object._retrieve_params = params
        return stripe_object

    def list_line_items(self, idempotency_key=None, **params):
        url = "/v1/quotes/{quote}/line_items".format(
            quote=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        resp = self.request("get", url, params, headers)
        stripe_object = util.convert_to_stripe_object(resp)
        stripe_object._retrieve_params = params
        return stripe_object

    @classmethod
    def _cls_pdf(
        cls,
        sid,
        api_key=None,
        idempotency_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        url = "%s/%s/%s" % (
            cls.class_url(),
            quote_plus(util.utf8(sid)),
            "pdf",
        )
        requestor = api_requestor.APIRequestor(
            api_key,
            api_base=ai21.upload_api_base,
            api_version=stripe_version,
            account=stripe_account,
        )
        headers = util.populate_headers(idempotency_key)
        response, _ = requestor.request_stream("get", url, params, headers)
        return response

    @util.class_method_variant("_cls_pdf")
    def pdf(
        self,
        api_key=None,
        api_version=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        version = api_version or stripe_version
        requestor = api_requestor.APIRequestor(
            api_key,
            api_base=ai21.upload_api_base,
            api_version=version,
            account=stripe_account,
        )
        url = self.instance_url() + "/pdf"
        return requestor.request_stream("get", url, params=params)
