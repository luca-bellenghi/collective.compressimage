from collective.compressimage.utilities.imageutilities import IImageUtility
from collective.compressimage.utilities.imageutilities import ImageUtility
from zope.component import getUtility
from zope.component import provideUtility
import os
import unittest


def dummy_image(filename=u'image.jpg'):
    from plone.namedfile.file import NamedBlobImage
    filename = os.path.join(os.path.dirname(__file__), filename)
    with open(filename, 'rb') as f:
        image_data = f.read()
    return NamedBlobImage(
        data=image_data,
        filename=filename
    )


class Utility(unittest.TestCase):

    def setUp(self):
        self.utility = ImageUtility()
        provideUtility(self.utility, IImageUtility)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Image', 'image')
        image = self.portal['image']
        image.title = 'My Image'
        image.description = 'This is my image.'
        image.image = dummy_image()
        self.image = image


    def test_image_info(self):
        import pdb;pdb.set_trace()
