from zope.interface import alsoProvides
from zope import schema
from plone.directives import form
from plone.autoform.interfaces import IFormFieldProvider
from z3c.form.interfaces import IEditForm, IAddForm

from upfront.mxitup import MessageFactory as _


class IMxitChatroom(form.Schema):
    """
       Marker/Form interface.
    """
    form.fieldset(
        'settings',
        label=_(u'Settings'),
        fields=['clientid', 'clientsecret'],
        )

    clientid = schema.Text(
           title = _(u"label_clientid", default=u"Client id"),
           required=True,
           )

    clientsecred = schema.Text(
           title = _(u"label_clientsecret", default=u"Client secret"),
           required=True,
           )

    form.omitted(['clientid', 'clientsecret'])
    form.no_omit(IEditForm, ['clientid', 'clientsecret'])
    form.no_omit(IAddForm, ['clientid', 'clientsecret'])

alsoProvides(IMxitChatroom, IFormFieldProvider)
