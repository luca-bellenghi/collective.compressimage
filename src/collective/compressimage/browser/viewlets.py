from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from collective.compressimage.utilities.imageutilities import IImageUtility
from plone import api
from plone.app.layout.viewlets import ViewletBase
from zope.component import getUtility
import

class ImageAlertViewlet(ViewletBase):
    """
    Viewlet showing information about the possibility to compress image.
    Allow to access the `compress image view`
    """

    index = ViewPageTemplateFile('templates/alert_image_viewlet.pt')
    info = {}
    treshold = 30

    def update(self):
        super(ImageAlertViewlet, self).update()
        self.image_utility = getUtility(IImageUtility)

    def show(self):
        """
        Called from template to check if viewlete need to be shown
        """
        permission = self.check_permission()
        size = self.check_size()
        return permission and size

    def check_permission(self):
        """
        Check if current user have permission to modify the content: this view
        allow to access the `compress image view` and here user can compress
        the image
        """
        return api.user.has_permission(
            'Modify portal content',
            user=api.user.get_current(),
            obj=self.context)

    def check_size(self):
        """
        Check if compression allow to gain at least 30% of image size
        """
        self.info = self.image_utility.get_image_info(self.context.image)
        percentage = (float(self.info['new_size']) * 100.0) / ((self.info['old_size']))
        saved_percentage = 100.0 - percentage
        return saved_percentage > self.treshold