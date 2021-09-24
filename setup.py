import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="codino",
    version="0.0.1",
    author="David Zhang",
    author_email="dyzhang32@gmail.com",
    description="Calculating AA frequencies from codon frequencies and "
                "vice-versa",
    long_description=long_description,
    long_description_content_type="text/md",
    url="https://github.com/dzhang32/codino",
    project_urls={
        "Bug Tracker": "https://github.com/dzhang32/codino/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.8",
)
