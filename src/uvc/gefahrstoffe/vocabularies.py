# -*- coding:utf-8 -*-

from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from uvc.gefahrstoffe import _

hskategorieVocabulary = SimpleVocabulary((
    SimpleTerm(u"id_wasserloeslich", u"wasserloeslich", u"gegen wasserlösliche Arbeitsstoffe"),
    SimpleTerm(u"id_nichtwasserloeslich", u"nichtwasserloeslich", u"gegen wasserunlösliche Arbeitsstoffe"),
    SimpleTerm(u"id_wechselnd", u"wechselnd", u"gegen wechselnde Arbeitsstoffe")
    ))

bgetembranchen = SimpleVocabulary((
    SimpleTerm(value=u'druckundpapier', token=u'druckundpapier', title=u'Druck und Papierverarbeitung'),
    SimpleTerm(value=u'elektrohandwerke', token=u'elektrohandwerke', title=u'Elektrohandwerke'),
    SimpleTerm(value=u'elektrotechnische industrie', token=u'elektrotechnische industrie', title=u'Elektrotechnische Industrie'),
    SimpleTerm(value=u'feinmechanik', token=u'feinmechanik', title=u'Feinmechanik'),
    SimpleTerm(value=u'textilundmode', token=u'textilundmode', title=u'Textil und Mode'),
    ))
