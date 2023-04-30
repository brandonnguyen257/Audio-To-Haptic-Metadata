from setuptools import setup, find_packages

#we pull the same depdencies from requirements.txt into setup.py
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="Haptic-Metadata-Generation",
    version="0.1.0",
    author="Brandon Nguyen",
    author_email="brandonnguyen257@gmail.com",
    description="Code for generating metadata for haptic data",
    packages=find_packages(),
    install_requires=requirements,
)
