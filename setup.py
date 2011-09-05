from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='TabularEventsView',
      version=version,
      description="Tabular Events View",
      long_description=open("README.txt").read() + "\n" +
                       open("CHANGES.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author="Paul Rentschler",
      author_email="paul@rentschler.ws",
      url='http://paul.rentschler.ws',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone>=4.0',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
