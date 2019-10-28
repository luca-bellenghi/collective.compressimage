from plone.app.layout.viewlets.tests.base import ViewletsTestCase
from plone.app.testing import login
from plone.app.testing import TEST_USER_NAME, TEST_USER_ID
from plone.app.testing import setRoles
from plone import api
from collective.compressimage.browser.viewlets import ImageAlertViewlet


def patch_image_info():
    return {'new_size': 1, 'old_size': 100}


class TestImageAlertViewlet(ViewletsTestCase):
    """
    Test the alert viewlet
    """

    def setUp(self):
        super(TestImageAlertViewlet, self).setUp()
        self.folder.invokeFactory('Image', 'img1', title='Image 1')
        self.context = self.folder['img1']
        self.portal = self.layer['portal']
        self.username = 'visitor'
        properties = {
            'username': self.username,
            'fullname': self.username,
            'email': 'visitor@mymail.com'
        }
        pr = api.portal.get_tool('portal_registration')
        pr.addMember(self.username, self.username, properties=properties)

    def _get_viewlet(self):
        request = self.app.REQUEST
        viewlet = ImageAlertViewlet(self.context, request, None, None)
        viewlet.update()
        viewlet.image_info = patch_image_info
        return viewlet

    def test_dont_show_alert_if_not_have_permission(self):
        login(self.portal, self.username)
        setRoles(self.portal, self.username, ['Member', ])
        viewlet = self._get_viewlet()
        self.assertFalse(viewlet.show())

    def test_show_alert_if_have_permission(self):
        login(self.portal, TEST_USER_NAME)
        setRoles(self.portal, TEST_USER_ID, ['Editor', ])
        viewlet = self._get_viewlet()
        self.assertTrue(viewlet.show())




