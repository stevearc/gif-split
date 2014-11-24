""" Setup file. """
import os

from setuptools import setup, find_packages


HERE = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(HERE, 'README.rst')).read()
CHANGES = open(os.path.join(HERE, 'CHANGES.rst')).read()

REQUIREMENTS = [
    'paste',
    'Pillow',
    'pyramid',
    'pyramid_duh',
    'pyramid_jinja2',
    'requests',
]

TEST_REQUIREMENTS = []

if __name__ == "__main__":
    setup(
        name='gif_split',
        version="0.1",
        description='Webserver to split gifs into spritesheets',
        long_description=README + '\n\n' + CHANGES,
        classifiers=[
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Framework :: Pyramid',
        ],
        author='Steven Arcangeli',
        author_email='stevearc@stevearc.com',
        url='',
        platforms='any',
        include_package_data=True,
        zip_safe=False,
        packages=find_packages(),
        entry_points={
            'paste.app_factory': [
                'main = gif_split:main',
            ],
        },
        install_requires=REQUIREMENTS,
        tests_require=REQUIREMENTS + TEST_REQUIREMENTS,
    )
