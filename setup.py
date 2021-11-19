from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='simpleLogicParser',
    version='1.0.0',
    description='A simple logic grammar parser using Python and Antlr',
    long_description=long_description,
    long_description_content_type='text/markdown',  
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6, <4',
    install_requires=['argparse','antlr4-python3-runtime','peppercorn'],
    extras_require={  # Optional
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    author='Anton Svystunov',
    author_email='antonsvistunov99@gmail.com',
    url='https://github.com/AntonSvystunov',
    entry_points={
        'console_scripts': [
            'simpleLogicParser=simpleLogicParser:main',
        ],
    }
)