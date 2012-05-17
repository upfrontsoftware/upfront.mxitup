from Acquisition import aq_inner
from zope.interface import Interface
from five import grok
from zope.component import getMultiAdapter
from Products.Archetypes.utils import shasattr

from plone.app.layout.viewlets.interfaces import IBelowContent

from upfront.mxitup.behaviors.mxit_chatroom import IMxitChatroom


grok.context(Interface)
grok.templatedir('templates')

class MxitChatroomLink(grok.Viewlet):
    """ Render a mxit specific chatroom link """

    grok.viewletmanager(IBelowContent)
    
    def update(self):
        self.can_show = False
        self.chatroom = None
        try:
            # first try the behavior
            adapter = IMxitChatroom(self.context)
            self.chatroom = adapter.chatroom
            self.can_show = adapter and True or False
        except TypeError:
            # so the behavior didn't work, now check the schema extender
            self.can_show = shasattr(self.context, 'chatroom') and True or False
            if self.can_show:
                self.chatroom = self.context.chatroom

    def can_show(self):
        """ Only show the link if the behavior is enabled.
            We take both the dexterity behavior and the schema extender
            into consideration.
        """
        return self.can_show

    def chatroom(self):
        import pdb;pdb.set_trace()
        return self.chatroom
