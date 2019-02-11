from io import open

from setuptools import find_packages, setup

with open('lda2vec/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('=')[1].strip(' \'"')
            break
    else:
        version = '0.0.1'

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

REQUIRES = []

setup(
    name='pylda2vec',
    version=version,
    description='Mixing Dirichlet Topic Models and Word Embeddings to Make lda2vec',
    long_description=readme,
    author='ONLPS',
    author_email='royalkingpin@gmail.com',
    maintainer='ONLPS',
    maintainer_email='royalkingpin@gmail.com',
    url='https://github.com/ONLPS/lda2vec',
    license='MIT',

    keywords=[
        'lda', 'topic-models', 'text', 'text processing', 'nlp'
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ],

    install_requires=REQUIRES,
    tests_require=['coverage', 'pytest'],

    packages=find_packages(),
)
