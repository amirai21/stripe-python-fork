# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from ai21.api_resources.abstract import CreateableAPIResource


class ThreeDSecure(CreateableAPIResource):
    OBJECT_NAME = "three_d_secure"

    @classmethod
    def class_url(cls):
        return "/v1/3d_secure"
