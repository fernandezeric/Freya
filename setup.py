from setuptools import setup

# pip install -e .
setup(
      name='Freya',
      version='0.1.3.3',
      description='This is a Framework',
      url='',
      author='Jonimott de Malpais',
      author_email='',
      license='',
      packages=['Freya'],
      entry_points = {
            'console_scripts': ['freya-admin=Freya.freya:main'],
      },
      zip_safe=False,
      install_requires=['astropy==4.2',
                        'pandas==1.2.0',
                        'requests==2.25.1']
)
