.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

========================
collective.compressimage
========================

This product show on image content type a viewlet with information about image size 
and how much it can be compressed with PIL.

The goal is to allow editors to better manage images for the web.

Features
--------

- Current main feature is to select a compressed version for Image content type instance
- In the future it would be nice allow to compress every image field in every content types


Examples
--------

This add-on can be seen in action at the following sites:
- Is there a page on the internet where everybody can see the features?


Documentation
-------------

Full documentation for end users can be found in the "docs" folder, and is also available online at http://docs.plone.org/foo/bar


Translations
------------

This product has been translated into

- Klingon (thanks, K'Plai)


Installation
------------

Install collective.compressimage by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.compressimage


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.compressimage/issues
- Source Code: https://github.com/collective/collective.compressimage
- Documentation: https://docs.plone.org/foo/bar


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@example.com


License
-------

The project is licensed under the GPLv2.
