from pprint import pprint
from federal_register.client import FederalRegister

# Initialize the client.
federal_register_client = FederalRegister()

# Grab a specific document.
federal_document = federal_register_client.document_by_id(
    document_id='2020-17469',
    fields='all'
)
pprint(federal_document)

# Grab multiple documents by their IDs.
federal_documents = federal_register_client.documents_by_id(
    document_ids=['2020-17469', '2020-17393'],
    fields='all'
)
pprint(federal_documents)

# Grab Federal Register Agencies List..
federal_register_agencies = federal_register_client.agencies()

# Save to file.
federal_register_client.save_to_json(
    content=federal_register_agencies,
    file_name='samples/responses/agencies.jsonc'
)
pprint(federal_register_agencies)
