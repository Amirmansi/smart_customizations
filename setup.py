from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in smart_customizations/__init__.py
from smart_customizations import __version__ as version

setup(
	name="smart_customizations",
	version=version,
	description="Smart Customization",
	author="Peter Maged",
	author_email="eng.peter.maged@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
