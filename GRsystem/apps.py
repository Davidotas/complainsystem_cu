from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class SuitConfig(DjangoSuitConfig):
    layout='vertical'
    name = 'GRsystem'
class GrsystemConfig(AppConfig):
    name = 'GRsystem'
    
