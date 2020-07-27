import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='telegram-logger',
    version='0.0.2',
    author='Marko van Treeck',
    author_email='markovantreeck@gmail.com',
    description='Send logs to telegram',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/LocalToasty/TelegramLogger',
    packages=setuptools.find_packages(),
    scripts=['telegram-logger'],
    install_requires=['python-telegram-bot'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
