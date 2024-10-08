import os
from distutils.command.build import build

from django.core import management
from setuptools import find_packages, setup

try:
    with open(
        os.path.join(os.path.dirname(__file__), "README.rst"), encoding="utf-8"
    ) as f:
        long_description = f.read()
except Exception:
    long_description = ""


class CustomBuild(build):
    def run(self):
        management.call_command("compilemessages", verbosity=1)
        build.run(self)


cmdclass = {"build": CustomBuild}


setup(
    name="pretix_es_mail",
    version='1.0.0',
    description="Simple HTML Email Renderer for Pretix",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kongr45gpen/pretix-email-templates",
    author="Electroservices Team",
    author_email="electrovesta@gmail.com",
    license="Apache",
    install_requires=[],
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    cmdclass=cmdclass,
    entry_points="""
[pretix.plugin]
pretix_es_mail=pretix_es_mail:PretixPluginMeta
""",
)

