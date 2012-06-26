from setuptools import setup, find_packages


setup(
    name='django-custom_delete_selected',
    version='0.1',
    license='ISC',
    description='Customization of delete_selected ModelAdmin action for '
        'post and pre operations.',
    url='https://github.com/saippuakauppias/django-custom_delete_selected',
    author='Denis Veselov',
    author_email='progr.mail@gmail.com',
    packages=find_packages(),
    install_requires=[
        'django'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
)