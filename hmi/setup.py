from setuphelpers import long_description
from setuptools import setup, find_namespace_packages

setup(
    name='hmi',
    version='0.0.1c',
    description='hmi principal',
    long_description=long_description(),
    url='',
    author='Lumensia Sensors S.L.',
    author_email='asaez@lumensia.com',
    license='Lumensia Sensors S.L. Copyright',
    classifiers=[
        'Development Status :: 4 - Beta',  # 3 - Alpha   4 - Beta   5 - Production/Stable
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='domoManu',
    packages=find_namespace_packages(exclude=["*respecto*"]),
    include_package_data=True,
)
