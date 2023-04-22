from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="Secrets-Creator",
    version="1.0",
    author="Cameron Trippick",
    install_requires=requirements,
    packages=['secrets_manager', 'secrets_manager.lib'],
    entry_points={
        'console_scripts': [
            'Secrets-Creator = secrets_manager.app:run',
        ]
    }
)