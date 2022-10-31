from setuptools import setup

setup(
    name="fsql",
    version="1.0",
    description="Fake SQL Insert Statement Generator",
    author="Babin Ion",
    author_email="owhy4100@gmail.com",
    packages=["fsql", "tests"],
    keywords="command line todo list",
    license="MIT",
    python_requires=">=3.10",
    extras_require={"tests": {"pytest==7.1.3", "pytest-mock==3.10.0"}},
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
    ],
    entry_points={
        "console_scripts": [
            "fsql = fsql.fsql:main",
        ],
    },
)
