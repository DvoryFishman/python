from setuptools import setup

setup(
    name='mini-wit',
    version='0.1.0',
    description='WIT - A simple version control system similar to Git',
    author='Student',
    py_modules=['main', 'wit', 'add_step', 'checkout_step', 'commit_step', 'init_step', 'status_step', 'FolderAndFile'],
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'wit=wit:cli',
        ],
    },
    python_requires='>=3.10',
)
