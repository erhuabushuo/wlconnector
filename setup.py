from setuptools import setup, find_packages


setup(
    name='wlconnector',
    version='0.1',
    description='Device communication server',
    author='Aidan He',
    author_email='erhuabushuo@gmail.com',
    url='https://github.com/erhuabushuo/wlconnector',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    platforms='all',
    # data_files=[
    #     ('/etc', ['wlconnector.ini'])
    # ],
    install_requires=[
        'uvloop',
        'aioredis',
        'click',
    ],
    classifiers=[
        'Development Status :: 3 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Communications',
        'Topic :: Internet'
    ],
    entry_points={
        'console_scripts': [
            'wlconnector = scripts.wlconnector_script:cli',
        ]
    },
    test_suite='nose.collector',
    tests_require=['nose'],
)
