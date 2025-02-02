# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from ai21 import util
from ai21.api_resources.abstract import UpdateableAPIResource
from ai21.api_resources.account import Account
from ai21.six.moves.urllib.parse import quote_plus


class Person(UpdateableAPIResource):
    OBJECT_NAME = "person"

    def instance_url(self):
        token = util.utf8(self.id)
        account = util.utf8(self.account)
        base = Account.class_url()
        acct_extn = quote_plus(account)
        extn = quote_plus(token)
        return "%s/%s/persons/%s" % (base, acct_extn, extn)

    @classmethod
    def modify(cls, sid, **params):
        raise NotImplementedError(
            "Can't modify a person without an account"
            "ID. Call save on account.persons.retrieve('person_id')"
        )

    @classmethod
    def retrieve(cls, id, api_key=None, **params):
        raise NotImplementedError(
            "Can't retrieve a person without an account"
            "ID. Use account.persons.retrieve('person_id')"
        )
