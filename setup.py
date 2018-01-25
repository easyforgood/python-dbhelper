from distutils.core import setup

files = ["things/*"]
dependson = [
        "mysqlclient",
        "pymongo"
]

setup(
    name="my-dbhelper",
    version="v1.0.0",
    description="",
    author="Sip Peng",
    author_email="siplexy.pi@outlook.com",
    packages=['dbhelper'],
    package_data={'package': files},
    long_description="""Really long text here.""",
    install_requires=dependson)
