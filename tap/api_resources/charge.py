from .abstract import ListeableAPIResource
from .abstract import UpdateableAPIResource
from .abstract import CreateableAPIResource
import tap

@tap.api_resources.abstract.nested_resource_class_methods(
    'charges',
    operations=['create', 'retrieve', 'list']
)
class Charge(CreateableAPIResource,
             UpdateableAPIResource,
             ListeableAPIResource):

    OBJECT_NAME = 'charge'
