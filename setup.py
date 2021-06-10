import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dj-gravatar",
    version="0.0.2",
    keywords="django gravatar avatar",
    author="Sourav Das",
    author_email="souravdas.sd20@gmail.com",
    description="Use Gravatar in a Django Website",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PhysicistSouravDas/dj-gravatar",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    project_urls={
        'Tracker': 'https://github.com/PhysicistSouravDas/dj-gravatar/issues',
    },
    python_requires='>=3.6',
    install_requires=["django>=2.1"],
)