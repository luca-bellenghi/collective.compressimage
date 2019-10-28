from PIL import Image
from zope import interface
from zope.interface import implementer, Interface
try:
    from cStringIO import StringIO
except ImportError:
    from io import BytesIO as StringIO
import humanize


class IImageUtility(Interface):
    """
    """

@implementer(IImageUtility)
class ImageUtility(object):

    def get_image_info(self, image):
        pilimage = Image.open(StringIO(image.data)).convert("RGB")
        tempimage = StringIO()
        pilimage.save(tempimage,
                      'JPEG',
                      quality=85)
        new_size = tempimage.tell()
        return {'old_size_hr': humanize.naturalsize(image.size),
                'new_size_hr': humanize.naturalsize(new_size),
                'new_size': new_size,
                'old_size': image.size}
