# Federal Register Python API Client

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
- [Usage](#usage)
- [Support These Projects](#support-these-projects)

## Overview

This library is used to grab federal documents from the United States Federal Register.
Additionally, it will help simplify the process of building requests for the different
fields that can be returned for specific documents.

## Setup

Right now, the library is not hosted on **PyPi** so you will need to do a local
install on your system if you plan to use it in other scrips you use.

First, clone this repo to your local system. After you clone the repo, make sure
to run the `setup.py` file, so you can install any dependencies you may need. To
run the `setup.py` file, run the following command in your terminal.

```console
pip install -e .
```

This will install all the dependencies listed in the `setup.py` file. Once done
you can use the library wherever you want.

## Usage

Here is a simple example of using the `federal_register` library to grab a document
using the document number.

```python
from pprint import pprint
from federal_register.client import FederalRegister

# Initialize the client.
federal_register_client = FederalRegister()

# Grab a specific document.
federal_document = federal_register_client.document_by_id(
    document_id='2020-17469',
    fields='all'
)

# Print it out.
pprint(federal_document)
```

## Support These Projects

**Patreon:**
Help support this project and future projects by donating to my [Patreon Page](https://www.patreon.com/sigmacoding)
. I'm always looking to add more content for individuals like yourself, unfortuantely some of the APIs I would require
me to pay monthly fees.

**YouTube:**
If you'd like to watch more of my content, feel free to visit my YouTube channel [Sigma Coding](https://www.youtube.com/c/SigmaCoding).
