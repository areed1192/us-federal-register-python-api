import unittest

from unittest import TestCase
from configparser import ConfigParser
from federal_register.client import FederalRegister


class FederalRegisterSession(TestCase):

    """Will perform a unit test for the `FederalRegisterClient` session."""

    def setUp(self) -> None:
        """Set up the Client."""

        self.federal_client = FederalRegister()

    def test_creates_instance_of_session(self):
        """Create an instance and make sure it's a `FederalRegisterClient`."""

        self.assertIsInstance(self.federal_client, FederalRegister)

    def test_document_by_id_endpoint(self):
        """Test grabbing a document by ID."""

        # Grab a document by the ID.
        federal_document = self.federal_client.document_by_id(
            document_id='2020-17469',
            fields='all'
        )

        # Make sure we have a response.
        self.assertIsNotNone(federal_document)

        # And the document ID matches.
        self.assertEqual(federal_document['document_number'], '2020-17469')

    def test_documents_by_id_endpoint(self):
        """Test grabbing multiple public documents by ID."""

        # Grab a document by the ID.
        federal_documents = self.federal_client.documents_by_id(
            document_ids=['2020-17469', '2020-17393'],
            fields='all'
        )

        # Make sure we have a response.
        self.assertIsNotNone(federal_documents)

        # Make sure the counts match.
        self.assertEqual(federal_documents['count'], 2)

    def test_agencies_endpoint(self):
        """Test grabbing Federal Agencies."""

        # Grab the agencies
        federal_agencies = self.federal_client.agencies()

        # Make sure we have a response.
        self.assertIsNotNone(federal_agencies)

        # And the agency ID Matches.
        self.assertEqual(federal_agencies[0]['id'], 557)

    def test_agencies_by_slug_endpoint(self):
        """Test grabbing an agency by their ID."""

        # Grab the Agency.
        federal_agency = self.federal_client.agency_by_id(
            agency_slug='antitrust-modernization-commission'
        )

        # Make sure we have a response.
        self.assertIsNotNone(federal_agency)

        # And the agency ID Matches.
        self.assertEqual(federal_agency['id'], 24)

    def test_public_document_by_id_endpoint(self):
        """Test grabbing a public document by their ID."""

        # Grab the public document.
        public_document = self.federal_client.public_inspection_document_by_id(
            document_id='2020-17127'
        )

        # Make sure we have a response.
        self.assertIsNotNone(public_document)

        # And the document ID Matches.
        self.assertEqual(public_document['document_number'], '2020-17127')

    def test_public_documents_by_id_endpoint(self):
        """Test grabbing multiple public documents by their ID."""

        # Grab the public documents.
        public_documents = self.federal_client.public_inspection_documents_by_id(
            document_ids=['2020-17127', '2020-17520']
        )

        # Make sure we have a response.
        self.assertIsNotNone(public_documents)

        # And count is 2.
        self.assertEqual(public_documents['count'], 2)

    def test_public_documents_current_endpoint(self):
        """Test grabbing current public documents."""

        # Grab the current public documents.
        public_documents_current = self.federal_client.public_inspection_documents_current()

        # Make sure we have a response.
        self.assertIsNotNone(public_documents_current)

        # And make sure we have some results, this should return more than 10.
        self.assertGreaterEqual(public_documents_current['count'], 10)

    def test_suggested_searches_endpoint(self):
        """Test grabbing suggested searches."""

        # Grab the Suggested Searches.
        suggested_searches = self.federal_client.suggested_searches(
            sections_ids=['health-and-public-welfare']
        )

        # Make sure we have a response.
        self.assertIsNotNone(suggested_searches)

        # And make sure the Slug matches.
        self.assertEqual(
            suggested_searches['health-and-public-welfare'][0]['slug'],
            'health-care-reform'
        )

    def test_suggested_searches_by_id_endpoint(self):
        """Test grabbing suggested searches using the Slug ID."""

        # Grab the Suggested Searches by a Slug ID.
        suggested_searches = self.federal_client.suggested_searches_by_slug(
            slug_id="accountable-care-organizations"
        )

        # Make sure we have a response.
        self.assertIsNotNone(suggested_searches)

        # And make sure the Slug matches.
        self.assertEqual(
            suggested_searches['slug'],
            'accountable-care-organizations'
        )

    def test_documents_detailed_search_endpoint(self):
        """Test grabbing documents through a more complex query."""

        # Grab presidential documents.
        presidential_documents = self.federal_client.documents(
            presidents=['donald-trump']
        )

        # Make sure we have a response.
        self.assertIsNotNone(presidential_documents)

        # And make sure we have some results.
        self.assertGreaterEqual(presidential_documents['count'], 10)

    def tearDown(self) -> None:
        """Teardown the `FederalRegisterClient`."""

        del self.federal_client


if __name__ == '__main__':
    unittest.main()
