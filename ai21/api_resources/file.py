# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

import ai21
from ai21 import api_requestor
from ai21 import util
from ai21.api_resources.abstract import ListableAPIResource


class File(ListableAPIResource):
    OBJECT_NAME = "file"

    # This resource can have two different object names. In latter API
    # versions, only `file` is used, but since ai21-python may be used with
    # any API version, we need to support deserializing the older
    # `file_upload` object into the same class.
    OBJECT_NAME_ALT = "file_upload"

    @classmethod
    def class_url(cls):
        return "/v1/files"

    @classmethod
    def create(
        # 'api_version' is deprecated, please use 'stripe_version'
        cls,
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
        url = cls.class_url()
        supplied_headers = {"Content-Type": "multipart/form-data"}
        response, api_key = requestor.request(
            "post", url, params=params, headers=supplied_headers
        )
        return util.convert_to_stripe_object(
            response, api_key, version, stripe_account
        )


# For backwards compatibility, the `File` class is aliased to `FileUpload`.
FileUpload = File
