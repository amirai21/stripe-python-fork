from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource


class TaxCode(ListableAPIResource):
    OBJECT_NAME = "tax_code"
