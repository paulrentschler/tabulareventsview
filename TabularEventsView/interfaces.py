"""Define interfaces for your add-on.
"""

from zope.interface import Interface

class ITabularEventsView(Interface):
    """A layer specific for this add-on product.

    This interface is referred in browserlayers.xml.

    All views and viewlets register against this layer will appear on your Plone site
    only when the add-on installer has been run.
    """