from pprint import pprint
from federal_register.client import FederalRegister

# Initialize the client.
federal_register_client = FederalRegister()

# Grab a specific document.
federal_document = federal_register_client.grab_document_by_id(
    document_id='2020-17469',
    fields='all'
)

# Save to file.
federal_register_client.save_to_json(
    content=federal_document,
    file_name='samples/responses/document.jsonc'
)
pprint(federal_document)