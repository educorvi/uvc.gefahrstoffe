# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s uvc.gefahrstoffe -t test_gefahrstoff.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src uvc.gefahrstoffe.testing.UVC_GEFAHRSTOFFE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/uvc/gefahrstoffe/tests/robot/test_gefahrstoff.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a gefahrstoff
  Given a logged-in site administrator
    and an add gefahrstoff form
   When I type 'My gefahrstoff' into the title field
    and I submit the form
   Then a gefahrstoff with the title 'My gefahrstoff' has been created

Scenario: As a site administrator I can view a gefahrstoff
  Given a logged-in site administrator
    and a gefahrstoff 'My gefahrstoff'
   When I go to the gefahrstoff view
   Then I can see the gefahrstoff title 'My gefahrstoff'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add gefahrstoff form
  Go To  ${PLONE_URL}/++add++gefahrstoff

a gefahrstoff 'My gefahrstoff'
  Create content  type=gefahrstoff  id=my-gefahrstoff  title=My gefahrstoff

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the gefahrstoff view
  Go To  ${PLONE_URL}/my-gefahrstoff
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a gefahrstoff with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the gefahrstoff title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
