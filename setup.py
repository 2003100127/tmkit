from setuptools import setup, find_packages

setup(
    name="tmkitx",
    version="0.0.1",
    keywords=("pip", "tmkit"),
    description="TMKit",
    long_description="TMKit",
    license="GNU GENERAL V3.0",

    url="https://github.com/2003100127/tmkit",
    author="Jianfeng Sun",
    author_email="jianfeng.sun@ndorms.ox.ac.uk",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    python_requires='<3.8',
    install_requires=[
        'scikit-learn',
        'pandas',
        'numpy',
        'biopandas',
        'tmhmm.py',
        'xmltramp2==3.1.1',
        'biopython==1.79',
        'pyfiglet==0.8.post1',
    ],

)