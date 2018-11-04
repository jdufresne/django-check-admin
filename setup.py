from setuptools import setup

with open("README.rst") as fp:
    readme = fp.read()

setup(
    name="django-check-admin",
    version="0.9.0",
    description=(
        "A Django app to check that all models have been added to the Django "
        "admin site."
    ),
    long_description=readme,
    url="https://github.com/jdufresne/django-check-admin",
    author="Jon Dufresne",
    author_email="jon.dufresne@gmail.com",
    license="BSD",
    packages=["checkadmin"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    install_requires=["Django >= 1.11"],
)
