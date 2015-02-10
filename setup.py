from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='paster_ansible',
      version=version,
      description="Ansible 1.x Project Template",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='ansible paster',
      author='Kazushige TAKEUCHI',
      author_email='kazushige.takeuchi@gmail.com',
      url='http://graceful-life.hatenablog.com/',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
        "PasteScript>=1.3",
        "ansible>=1.8",
      ],
      entry_points="""
      # -*- Entry points: -*-
        [paste.paster_create_template]
        ansible=paster_ansible.template:AnsibleProjectTemplate

      """,
      )
