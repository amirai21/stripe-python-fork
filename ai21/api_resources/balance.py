# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from ai21.api_resources.abstract import SingletonAPIResource


class Balance(SingletonAPIResource):
    OBJECT_NAME = "balance"

    @classmethod
    def class_url(cls):
        return "/v1/balance"
