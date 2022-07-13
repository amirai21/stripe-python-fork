# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from ai21.api_resources.abstract import CreateableAPIResource
from ai21.api_resources.abstract import DeletableAPIResource
from ai21.api_resources.abstract import ListableAPIResource


class ApplePayDomain(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
):
    OBJECT_NAME = "apple_pay_domain"

    @classmethod
    def class_url(cls):
        return "/v1/apple_pay/domains"
