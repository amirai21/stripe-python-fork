# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from ai21.api_resources.abstract import CreateableAPIResource
from ai21.api_resources.abstract import DeletableAPIResource
from ai21.api_resources.abstract import ListableAPIResource
from ai21.api_resources.abstract import SearchableAPIResource
from ai21.api_resources.abstract import UpdateableAPIResource


class Product(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    SearchableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "product"

    @classmethod
    def search(cls, *args, **kwargs):
        return cls._search(search_url="/v1/products/search", *args, **kwargs)

    @classmethod
    def search_auto_paging_iter(cls, *args, **kwargs):
        return cls.search(*args, **kwargs).auto_paging_iter()
