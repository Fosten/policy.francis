from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='policy.francis',
    version=version,
    description="francis policy",
    long_description=open("README.txt").read() + "\n" +
                     open("CHANGES.txt").read(),
    # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
      "Framework :: Plone",
      "Programming Language :: Python",
      "Topic :: Software Development :: Libraries :: Python Modules",
      ],
    keywords='',
    author='WebLion Group, Penn State University',
    author_email='support@weblion.psu.edu',
    url='http://weblion.psu.edu/',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['policy'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
      'setuptools',
      # -*- Extra requirements: -*-
      'plonetheme.francis',
      'Products.PloneFormGen',
      'Products.RedirectionTool',
      'Products.FacultyStaffDirectory',
      'collective.plonetruegallery',
      'Products.BlingPortlet',
      'Products.ContentWellPortlets',
      ],
    entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
    )

