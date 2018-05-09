from setuptools import setup, find_packages
from setuptools.command.test import test


class BacklogTests(test):
    def finalize_options(self):
        test.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import nose
        nose.run(argv=['nosetests'])


tests_require = ['nose', 'coverage', 'unittest']
exec(open('backlogapi/version.py').read())

setup(
    name='pybacklog',
    version=globals()['__version__'],
    packages=find_packages(exclude=('tests', 'tests.*')),
    include_package_data=True,
    url='https://github.com/keinuma/backlogapi',
    license='MIT',
    author='Keisuke Numata',
    author_email='nununu.mono@gmail.com',
    description='Backlog client for Python',
    keywords='backlog backlogapi pybacklog',
    tests_require=tests_require,
    cmdclass={'test': BacklogTests},
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: Python Software Foundation License',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Intended Audience :: Developers',
        'Natural Language :: Japanese',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'requests',
    ],
)