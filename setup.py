from setuptools import setup,find_packages

# pip install -e .
setup(
      name='Freya_alerce',
      version='0.1.4.8.8',
      author='Jonimott de Malpais',
      author_email='',
      description='Freya is a Python framework that quick development queries in astronomical catalogs and use local or creating easy new API called FreyaAPI',
      url='',
      license='',
      packages=find_packages(),
      #include_package_data=True,
      package_data = {
            'Freya_alerce.core': ['*.txt'],
            'Freya_alerce.files.file_templates': ['*.zip']
      },
      entry_points = {
            'console_scripts': ['freya-admin=Freya_alerce.freya:Main.main'],
      },
      zip_safe=False,
      classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Natural Language :: English"

      ],
      test_suite="tests",
      python_requires='>=3.9',
      install_requires=[i.strip() for i in open("requirements.txt").readlines()]
)