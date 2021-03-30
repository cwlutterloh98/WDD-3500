from setuptools import setup, find_packages
requires = [
    'flask',
    'url_for'
]
# run setup for creating neccessary packages
setup(
    name='flask_first_app',
    version='0.0',
    description='My first Python web app built with Flask',
    author='<Your actual name here>',
    author_email='<Your actual e-mail address here>',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)