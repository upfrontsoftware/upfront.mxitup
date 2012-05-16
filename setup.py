from setuptools import setup, find_packages
import os

version = '0.1dev'

setup(name='upfront.mxitup',
      version=version,
      description="upfront.mxitup",
      long_description=open("README.md").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Upfront Systems',
      author_email='rijk@upfrontsystems.co.za',
      url='git://github.com/upfrontsystems/upfront.mxitup.git',
      license='GPL version 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['upfront'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.dexterity',
          'plone.app.registry',
          'collective.autopermission',
          'plone.behavior',
          'plone.directives.form',
          'zope.schema',
          'zope.interface',
          'zope.component',
          'rwproperty',
          # -*- Extra requirements: -*-
      ],
      extras_require={
        'test': [
          'plone.app.testing',
        ],
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      # The next two lines may be deleted after you no longer need
      # addcontent support from paster and before you distribute
      # your package.
      setup_requires=["PasteScript"],
      paster_plugins = ["ZopeSkel"],

      )
