from setuptools import setup, find_packages

setup(name="corelogic_pyclient",
      version="0.5.0",
      description="Python client for Interacting with coreLogic API - Property Data Reports & Analytics",
      url="https://github.com/danielfarahani/corelogic_pyclient",
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6',
      ],
      keywords='Real-estate proptech property',
      author="Daniel Farahani",
      author_email="danfarahani@gmail.com",
      license="MIT",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      )