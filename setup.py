from setuptools import setup, find_packages

setup(
    name='ib_0',
    version='0.1.0',
    packages=find_packages(),
    description='None',
    author='Pablo Jadzinsky',
    author_email='pjadzinsky@gmail.com',
    classifiers=[
      'Programming Language :: Python',
      'Programming Language :: Python :: 3.7',
      'Operating System :: OS Independent',
      'License :: OSI Approved :: MIT License',
      'Development Status :: 3 - Alpha',
      'Topic :: Office/Business :: Financial',
    ],
    install_requires=[
      'kaleido',
      'numpy',
      'pandas',
      'plotly',
      'pytest',
    ],
    #data_files=[
    #    ('crypto', ['credentials.yaml']),
    #    ('crypto/common', ['crypto/common/wallets.yaml'])
    #],
    # package_data={
    #     'crypto': ['exchanges/credentials.yaml', 'common/wallets.yaml']
    # }

    # rm -rf .local in aws if pip3 install giving segmentation fault
)
