from setuptools import setup, find_packages

setup(
    name='automatic1111-image-display',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
    ],
)
