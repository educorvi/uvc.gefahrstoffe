# -*- coding: utf-8 -*-
from uvc.gefahrstoffe.content.gefahrstoff import IGefahrstoff  # NOQA E501
from uvc.gefahrstoffe.testing import UVC_GEFAHRSTOFFE_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class GefahrstoffIntegrationTest(unittest.TestCase):

    layer = UVC_GEFAHRSTOFFE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_gefahrstoff_schema(self):
        fti = queryUtility(IDexterityFTI, name='gefahrstoff')
        schema = fti.lookupSchema()
        self.assertEqual(IGefahrstoff, schema)

    def test_ct_gefahrstoff_fti(self):
        fti = queryUtility(IDexterityFTI, name='gefahrstoff')
        self.assertTrue(fti)

    def test_ct_gefahrstoff_factory(self):
        fti = queryUtility(IDexterityFTI, name='gefahrstoff')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IGefahrstoff.providedBy(obj),
            u'IGefahrstoff not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_gefahrstoff_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='gefahrstoff',
            id='gefahrstoff',
        )

        self.assertTrue(
            IGefahrstoff.providedBy(obj),
            u'IGefahrstoff not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('gefahrstoff', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('gefahrstoff', parent.objectIds())

    def test_ct_gefahrstoff_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='gefahrstoff')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_gefahrstoff_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='gefahrstoff')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'gefahrstoff_id',
            title='gefahrstoff container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
