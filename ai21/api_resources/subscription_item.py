# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from ai21.api_resources.abstract import CreateableAPIResource
from ai21.api_resources.abstract import DeletableAPIResource
from ai21.api_resources.abstract import ListableAPIResource
from ai21.api_resources.abstract import UpdateableAPIResource
from ai21.api_resources.abstract import nested_resource_class_methods


@nested_resource_class_methods("usage_record", operations=["create"])
@nested_resource_class_methods(
    "usage_record_summary",
    operations=["list"],
    resource_plural="usage_record_summaries",
)
class SubscriptionItem(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "subscription_item"

    def usage_record_summaries(self, **params):
        """usage_record_summaries is deprecated, use SubscriptionItem.list_usage_record_summaries instead."""
        return self.request(
            "get", self.instance_url() + "/usage_record_summaries", params
        )
