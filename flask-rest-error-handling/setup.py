import setuptools

setuptools.setup(
    name="flask-rest-error-handling",
    version="3.1.0",
    packages=setuptools.find_packages(),
    author="Reece Dunham",
    author_email="me@rdil.rocks",
    url="https://github.com/RDIL/bluejay",
    description="Provides users with JSON responses for errors.",
    install_requires=["Flask"],
    license="MIT",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown"
)
