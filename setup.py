from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='diazotheme.framework.metro',
      version=version,
      description="A Diazo framework implementation for the Metro UI CSS framework",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # https://pypi.org/pypi?:action=list_classifiers
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: Theme",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='web zope plone theme diazo metro-ui css framework',
      author='Thijs Jonkman',
      author_email='t.jonkman@gmail.com',
      maintainer='Leonardo Caballero',
      maintainer_email='leonardocaballero@gmail.com',
      url='https://github.com/TH-code/diazotheme.framework.metro',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['diazotheme', 'diazotheme.framework'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'diazoframework.plone',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
