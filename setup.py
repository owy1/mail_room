from setuptools import setup


setup(
    name='mailroom',
    description="manages a donation 'database'",
    version='0.1',
    author="Ophelia and Ely",
    license='MIT',
    py_modules=['mailroom'],
    package_dir={'': 'src'},
    extras_require={'testing': ['pytest', 'pytest-cov', 'tox']},
    entry_points={'console_scripts': ['mailroom = mailroom:main']}
)
