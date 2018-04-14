from setuptools import setup

setup(
    name='flask-test',
    version='0.1',
    author='Dennis Vriend',
    author_email='dnvriend@gmail.com',
    description="A study project on Flask",
    licence='Apache 2.0',
    packages=['app'],
    url="https://github.com/dnvriend/flask-test",
    install_requires=[
        'flask'
    ],
    entry_points='''
        [console_scripts]
        flask-test=app.app:main
    ''',
)