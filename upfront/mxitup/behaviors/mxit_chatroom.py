from zope.interface import alsoProvides, implements
from zope.component import adapts
from zope import schema
from plone.directives import form
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider
from z3c.form.interfaces import IEditForm, IAddForm

from upfront.mxitup import MessageFactory as _


class IMxitChatroom(form.Schema):
    """
       Marker/Form interface.
    """
alsoProvides(IMxitChatroom, IFormFieldProvider)


class MxitChatroom(object):
    """
       Adapter for content 
    """
    implements(IMxitChatroom)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context
