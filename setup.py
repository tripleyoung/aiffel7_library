from setuptools import setup, find_packages

setup(
    name='aiffel7',
    version='0.2.2',
    packages=find_packages(),
    description='A simple Python library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='aiffel7_그루',
    author_email='your.email@example.com',
    url='https://github.com/dudnjsckrgo/aiffel7_library',
    license='LICENSE',
    install_requires=[
        # 필요한 의존성 패키지 나열
        'beautifulsoup4',  # This is the package name for bs4
        'requests'
    ],
    classifiers=[
        # PyPI 분류자
        # 참조: https://pypi.org/classifiers/
    ],
)
