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
    form.fieldset(
        'mxitup',
        label=_(u'Mxitup settings'),
        fields=['chatroom',],
        )

    chatroom = schema.TextLine(
           title = _(u"label_chatroom", default=u"Chatroom"),
           required=False,
           )

    form.omitted('chatroom')
    form.no_omit(IEditForm, 'chatroom')
    form.no_omit(IAddForm, 'chatroom')

alsoProvides(IMxitChatroom, IFormFieldProvider)
