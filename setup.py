#!/usr/bin/env python3
# -*- coding: utf-8 -*-"
"""
[pArAnoIA_Browser] by /psy (03c8.net)/ - 2020

You should have received a copy of the GNU General Public License along
with pArAnoIA-Browser; if not, write to the Free Software Foundation, Inc., 51
Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""
import sys

if sys.version_info[0] != 3:
    sys.exit("Sorry, pArAnoIA requires Python >= 3")
    
from setuptools import setup, find_packages

setup(
    name='pArAnoIA',
    version='0.2',
    license='GPLv3',
    author_email='epsylon@riseup.net',
    author='psy',
    description='pArAnoIA Browser',
    url='https://browser.03c8.net/',
    long_description=open('docs/README.txt').read(),
    packages=find_packages(),
    install_requires=['pygeoip >= 0.3.2', 'requests'],
    include_package_data=True,
    package_data={
        'core': ['geo/GeoLiteCity.dat', 'images/*.jpeg'],
    },
    entry_points={
        'console_scripts': [
            'paranoia=pArAnoIA:core.main',
        ],
        'gui_scripts': [
            'paranoia=pArAnoIA:core.main',
        ],
    },
    keywords='Toolkit Browser Privacy pArAnoIA',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "Environment :: Web Environment",
        "Environment :: Console", 
        "Intended Audience :: System Administrators",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Programming Language :: Python :: 3',
        "Topic :: Internet", 
        "Topic :: Security", 
        "Topic :: System :: Networking",
      ],
      zip_safe=False
)
