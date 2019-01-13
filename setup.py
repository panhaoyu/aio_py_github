import setuptools
import aio_py_github

with open('README.md', 'r') as file:
    long_description = file.read()

module = aio_py_github
setuptools.setup(
    name=module.__name__,
    version=module.__version__,
    author=module.__author__,
    author_email='haoyupan@aliyun.com',
    description=module.__description__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/panhaoyu/aio_py_github',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
