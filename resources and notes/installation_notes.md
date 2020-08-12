# Python Package Installation

Once we build our library we are probably going to want and distribute it so other people can use it. Now at this point
I think it pays to define some terms before we continue. To start out, I will be referrring to my `td` client as a
package. A `package`, is simply a collection of python modules. A `module` is simply a python script. Technically we
have another level, a library. A `library` is a colleciton of various packages, however, conceptually there is no difference
between a library and a package.

## Step 1: Install `setuptools`

We will be using the `setuptools` module to package our modules. If you don't have have `setuptools` installed you'll
need to install it. To install it, run the following command in your console.

```console
pip install setuptools wheel
```

If you already have you'll want to make sure you're on the latest version, so make sure to update it using the following commands:

```console
pip install --upgrade setuptools wheel
```

## Step 2: Install `twine`

Twine is the primary tool developers use to upload packages to the Python Package Index or other Python package indexes. It is a
command-line program that passes program files and metadata to a web API. Developers use it because it’s the official PyPI upload
tool, it’s fast and secure, it’s maintained, and it reliably works. To install `twine`, run the following command:

```console
pip install twine
```

if you already have ir you'll want to make sure you're on the latest version, so make sure to update it using the following commands:

```console
pip install --upgrade twine
```

## Step 3: Build our Distribution Package

Now that we have everything installed, we can build or distribution package. To build our distribution pacakge run the following command:

```console
python setup.py sdist bdist_wheel
```

This will generate a distrubtion archives in the _dist_ folder. In fact, if you look in your directory you should see a few new folders
one called _dist_ and one called _build_. These were generated when we ran the command.

## Step 4: Upload our Distribution Pacakge to PyPi test Index

Before you run this command you need to have an account registered with PyPi, to register an account go to this
[link](https://test.pypi.org/account/register). After you register your account you'll want an access token so that way you can upload
distribtions to the index.

To upload the distribution run the following command:

```console
twine upload --repository testpypi --config-file pypirc dist/*
```

```console
twine upload --repository pypi --config-file pypirc dist/*
```

Once uploaded your package should be viewable on TestPyPI, for example, <https://test.pypi.org/project/example-pkg-YOUR-USERNAME-HERE>
