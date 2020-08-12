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

To **install** the library, run the following command from the terminal.

```console
pip install federal-register
```

To **upgrade** the library, run the following command from the terminal.

```console
pip install --upgrade federal-register
```

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
