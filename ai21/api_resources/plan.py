# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from ai21.api_resources.abstract import CreateableAPIResource
from ai21.api_resources.abstract import DeletableAPIResource
from ai21.api_resources.abstract import ListableAPIResource
from ai21.api_resources.abstract import UpdateableAPIResource


class Plan(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "plan"
