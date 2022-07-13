# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from ai21.api_resources.abstract import CreateableAPIResource
from ai21.api_resources.abstract import ListableAPIResource
from ai21.api_resources.abstract import UpdateableAPIResource


class FileLink(
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "file_link"
