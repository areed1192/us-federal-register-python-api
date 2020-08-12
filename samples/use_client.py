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

# Grab Federal Register Agencies List.
federal_register_agencies = federal_register_client.agencies()
pprint(federal_register_agencies)

# Grab a Federal Register Agency by ID.
federal_register_agencies = federal_register_client.agency_by_id(
    agency_slug='antitrust-modernization-commission'
)
pprint(federal_register_agencies)

# Grab a public inspection document by their ID.
public_document = federal_register_client.public_inspection_document_by_id(
    document_id='2020-17127'
)
pprint(public_document)

# Grab multiple public inspection documents by their IDs.
public_documents = federal_register_client.public_inspection_documents_by_id(
    document_ids=['2020-17127', '2020-17520']
)
pprint(public_documents)

# Grab Federal Register Agencies List..
public_documents_current = federal_register_client.public_inspection_documents_current()

# Save to file.
federal_register_client.save_to_json(
    content=public_documents_current,
    file_name='samples/responses/public_documents_current.jsonc'
)
pprint(public_documents_current)