# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Container
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer

from uvc.gefahrstoffe.vocabularies import hskategorieVocabulary, bgetembranchen

from uvc.gefahrstoffe import _

class IGefahrstoff(model.Schema):
    """ Marker interface and Dexterity Python Schema for Gefahrstoff
    """

    title = schema.TextLine(title=_(u"Name des Gefahrstoffes"))

    description = schema.Text(title=_(u"Nähere Angaben zum Gefahrstoff"), required=False)

    casnr = schema.TextLine(title=_(u"CAS-Nummer"), required=False)

    hskategorie = schema.Choice(title=_(u"Hautschutzmittelgruppe"), vocabulary=hskategorieVocabulary, required=False)

    hersteller = schema.TextLine(title=_(u"Name des Herstellers"), required=False)

    branche = schema.List(title=_(u"Branchen, in denen der Gefahrstoff eingesetzt wird"),
                          value_type=schema.Choice(vocabulary=bgetembranchen),
                          required = False)

@implementer(IGefahrstoff)
class Gefahrstoff(Container):
    """
    """
