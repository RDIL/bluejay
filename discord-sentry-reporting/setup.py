import setuptools

setuptools.setup(
    name="discord-sentry-reporting",
    version="1.0.0",
    packages=setuptools.find_packages(),
    author="Reece Dunham",
    author_email="me@rdil.rocks",
    url="https://github.com/RDIL/bluejay",
    description="A small compatibility library that provides functionality to report errors from discord.py to Sentry.",  # noqa
    install_requires=["discord>=1.0.0", "sentry_sdk"],
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    license="MIT"
)