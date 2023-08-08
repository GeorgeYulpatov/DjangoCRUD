from setuptools import setup, find_packages

setup(
    name='m3_project',
    version='1.0',
    author='tatarin10703',
    url='https://github.com/tatarin10703/DjangoCRUD',
    packages=find_packages(),
    install_requires=[
        'django==2.2.2',
        'm3-django-compat==1.9.2',
        'm3-objectpack==2.2.47'
    ],

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Operating System :: Ubuntu',
    ],
)
