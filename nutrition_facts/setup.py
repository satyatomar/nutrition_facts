from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="nutrition-facts",
    version="0.0.1",
    description="A Python package to get nutrition facts.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/satyatomar/nutrition_facts.git",
    author="satyapal singh tomar",
    author_email="er.satyatomar@gmail.com",
    py_modules=["nutrition_facts"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    license="MIT",
    package_dir={'': 'nutrition--facts'},
)
