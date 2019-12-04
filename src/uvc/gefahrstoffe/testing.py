# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import uvc.gefahrstoffe


class UvcGefahrstoffeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=uvc.gefahrstoffe)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'uvc.gefahrstoffe:default')


UVC_GEFAHRSTOFFE_FIXTURE = UvcGefahrstoffeLayer()


UVC_GEFAHRSTOFFE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(UVC_GEFAHRSTOFFE_FIXTURE,),
    name='UvcGefahrstoffeLayer:IntegrationTesting',
)


UVC_GEFAHRSTOFFE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(UVC_GEFAHRSTOFFE_FIXTURE,),
    name='UvcGefahrstoffeLayer:FunctionalTesting',
)


UVC_GEFAHRSTOFFE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        UVC_GEFAHRSTOFFE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='UvcGefahrstoffeLayer:AcceptanceTesting',
)
