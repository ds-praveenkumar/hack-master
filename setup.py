from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='hackmaster',
      version='1.0',
      description='develop baseline models for ML competition',
      author='Praveen Kumar',
      author_email='praveenkr2208@gmail.com',
      url='https://github.com/ds-praveenkumar/hack-master',
      packages=find_packages(),
      install_requires=required,
     )
