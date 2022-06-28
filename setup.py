import setuptools
from setuptools import setup

setup(
    name='quask',
    version='0.1.0',
    description='Quantum Advantage Seeker withKernels',
    url='https://github.com/QML-HEP/QuASK',
    author='Massimiliano Incudini <massimiliano.incudini@univr.it>, Francesco Di Marcantonio <francesco.di.marcantonio@cern.ch>, Michele Grossi <michele.grossi@cern.ch>',
    license='Apache License Version 2.0',
    packages=setuptools.find_packages(),
    python_requires='>=3.9.10',
    install_requires=[
        'openml',
        'numpy',
        'scikit-learn',
        'scipy',
        'PennyLane',
        'PennyLane-qiskit',
        'jax'
    ],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: Unix',
        'Topic :: Scientific/Engineering :: Physics',
        'Programming Language :: Python :: 3.9',
    ],
)
