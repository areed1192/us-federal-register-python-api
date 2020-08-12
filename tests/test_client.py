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

    def test_document_id_endpoint(self):
        """Test grabbing a document by ID."""

        # Grab a document by the ID.
        federal_document = self.federal_client.grab_document_by_id(
            document_id='2020-17469',
            fields='all'
        )

        # Make sure we have a response.
        self.assertIsNotNone(federal_document)

        # And the document ID matches.
        self.assertEqual(federal_document['document_number'], '2020-17469')

    def tearDown(self) -> None:
        """Teardown the `FederalRegisterClient`."""

        del self.federal_client


if __name__ == '__main__':
    unittest.main()
