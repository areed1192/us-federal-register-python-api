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

# Grab the current public documents.
public_documents_current = federal_register_client.public_inspection_documents_current()
pprint(public_documents_current)

# Grab the suggested searches for the Health and Public Welfare.
suggested_searches = federal_register_client.suggested_searches(
    sections_ids=['health-and-public-welfare']
)
pprint(suggested_searches)

# Grab the suggested searches for the Accountable Care Organization Slug.
suggested_searches_by_ids = federal_register_client.suggested_searches_by_slug(
    slug_id='accountable-care-organizations'
)
pprint(suggested_searches_by_ids)

# Search for documents using more specific criterias, like presidential names.
documents_search = federal_register_client.documents(
    presidents=['donald-trump']
)
pprint(documents_search)

# Search for presidential documents and group the count of documents by daily counts.
documents_search = federal_register_client.documents_facets(
    facet='daily',
    presidents=['donald-trump']
)
pprint(documents_search)

# Search for public documents using a more specific query, like the date they were available on.
public_documents = federal_register_client.public_inspection_documents(
    available_on='2020-08-10'
)
pprint(public_documents)
