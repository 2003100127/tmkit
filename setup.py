from setuptools import find_packages, setup

setup(
    name="tmkit",
    version="0.0.5",
    keywords=("pip", "tmkit"),
    description="TMKit",
    long_description="TMKit",
    license="GNU GENERAL V3.0",
    url="https://github.com/2003100127/tmkit",
    author="Jianfeng Sun",
    author_email="jianfeng.sun@ndorms.ox.ac.uk",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "": [".env", "*.pl"],
    },
    platforms="any",
    python_requires=">3=.10",
    install_requires=[
        "scikit-learn",
        "pandas",
        "numpy",
        "openpyxl",
        "biopandas",
        "pypdb==2.2",
        "xmltramp2==3.1.1",
        "biopython==1.79",
        "pyfiglet==0.8.post1",
    ],
)
