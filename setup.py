from setuptools import setup, find_packages


with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pppy',
    version="0.0.1",
    description='An implementation of the Performance Profile in Python.',
    long_description=long_description,
    author='Sakai Hiroyuki',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)