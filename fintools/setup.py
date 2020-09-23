from setuptools import setup, find_packages


with open("README.md") as file:
    readme = file.read()

setup(
    name="fintools",
    version="0.1.0",
    description="Financial Tools",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="iteso",
    classifiers=[
    ],
    package_dir={
        "": "src"
    },
    package_data={
        "": [

        ]
    },
    packages=find_packages(where="src"),
    include_package_data=True,
    scripts=[
        "bin/fintools"
    ],
    install_requires=[

    ],
    python_requires=">=3.5, <4",
    license=""
)
