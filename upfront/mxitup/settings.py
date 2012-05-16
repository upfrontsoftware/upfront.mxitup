from zope.interface import Interface
from zope import schema
from five import grok
from Products.CMFCore.interfaces import ISiteRoot

from plone.z3cform import layout
from plone.directives import form
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from upfront.mxitup import MessageFactory as _

class IMxitupSettings(form.Schema):
    """ Define mxitup settings schema """

    clientid = schema.TextLine(
           title = _(u"label_clientid", default=u"Client id"),
           required=True,
           )

    clientsecret = schema.TextLine(
           title = _(u"label_clientsecret", default=u"Client secret"),
           required=True,
           )


class MxitupSettingsForm(RegistryEditForm):
    """
    """
    schema = IMxitupSettings
    label = u"Mxitup settings"


class MxitupSettingsView(grok.CodeView):
    """
    """
    grok.name("mxitup-settings")
    grok.context(ISiteRoot)

    def render(self):
        view_factory = layout.wrap_form(
            MxitupSettingsForm, ControlPanelFormWrapper)
        view = view_factory(self.context, self.request)
        return view()
