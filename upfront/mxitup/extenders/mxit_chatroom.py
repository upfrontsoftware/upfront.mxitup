from zope.interface import implements

from Products.Archetypes.Widget import StringWidget
from Products.Archetypes.public import StringField

from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import ISchemaExtender

import logging
LOG = logging.getLogger('MxitChatroomExtender')

class _MxitChatroomExtensionField(ExtensionField, StringField): pass

class MxitChatroomExtender(object):
    implements(ISchemaExtender)

    fields = [
        _MxitChatroomExtensionField(
            "chatroom",
            default = False,
            widget = StringWidget(
                label=u"Chatroom",
                description=u"Chatroom",
            ),
            schemata='Mxitup settings',
        ),
    ]


    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields

