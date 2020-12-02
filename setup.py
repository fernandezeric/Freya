from setuptools import setup

# pip install -e .
setup(
      name='Freya',
      version='0.1.2.1',
      description='This is a Framework',
      url='',
      author='Jonimott de Malpais',
      author_email='',
      license='La que ALeRCE decida',
      packages=['Freya'],
      entry_points = {
            'console_scripts': ['freya-admin=Freya.freya:main'],
      },
      zip_safe=False,
      install_requires=['astropy','pandas'] # change to file
)