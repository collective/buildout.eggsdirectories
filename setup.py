from setuptools import setup, find_packages

version = '1.0'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(
    name='buildout.eggsdirectories',
    version=version,
    description=(
        "zc.buildout extension to include supplementary preloaded "
        "egg-directories"
    ),
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
    ],
    keywords='',
    author='',
    author_email='',
    url='http://github.com/collective/buildout.eggsdirectories',
    license='gpl',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    namespace_packages=['buildout'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
    entry_points="""
[zc.buildout.extension]
buildout.eggsdirectories = buildout.eggsdirectories:extend
    """,
)
