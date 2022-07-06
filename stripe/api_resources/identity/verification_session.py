# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import custom_method


@custom_method("cancel", http_verb="post")
@custom_method("redact", http_verb="post")
class VerificationSession(
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "identity.verification_session"

    def cancel(self, idempotency_key=None, **params):
        url = "/v1/identity/verification_sessions/{session}/cancel".format(
            session=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def redact(self, idempotency_key=None, **params):
        url = "/v1/identity/verification_sessions/{session}/redact".format(
            session=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self
