import json
import pathlib
import requests

from typing import List
from typing import Dict
from typing import Union

from federal_register.fields import document_fields


class FederalRegister():

    def __init__(self) -> None:
        """Initializes the `FederalRegisterClient` object."""

        self.api_base_url = 'https://www.federalregister.gov/api'
        self.api_version = 'v1'

    def __repr__(self) -> str:
        """Represents the string representation of the client object.

        Returns:
        ----
        (str): The string representation.
        """
        return "<FederalRegisterClient Connected: True>"

    def save_to_json(self, content: Union[List, Dict], file_name: str, folder: str = None) -> str:

        file_path = pathlib.Path(file_name)

        with open(file=file_path, mode='w+') as data_file:
            json.dump(obj=content, fp=data_file, indent=2)

    def _build_url(self, endpoint: str, arguments: List[str]) -> str:
        """Builds a full URL for the API Client.

        Arguments:
        ----
        endpoint (str): The endpoint to be requested.

        arguments (List[str]): Any additional arguments needed to be
            joined with the URL.

        Returns:
        ----
        str: The full `HTTPS` url.
        """

        full_url = '/'.join(
            [self.api_base_url, self.api_version, endpoint] + arguments
        )
        full_url_with_format = full_url + '.json'

        return full_url_with_format

    def _make_request(self, url: str, method: str, params: dict) -> dict:
        """Used to make all the request for the client.

        Arguments:
        ----
        method (str): [description]

        params (dict): [description]

        Returns:
        ----
        dict: The JSON content parsed.
        """

        # Make the request.
        if method == 'get':
            response = requests.get(url=url, params=params)

        # If it's a good response, send back.
        if response.ok:
            return response.json()

    def grab_document_by_id(self, document_id: int, fields: List[str]) -> dict:
        """Fetch a single Federal Register document by their ID.

        Arguments:
        ----
        document_id (int): Federal Register document number.

        fields (List[str]): Which attributes of the documents to return; by 
            default, a reasonable set is returned, but a user can customize 
            it to return exactly what is needed.

        Returns:
        ----
        dict: The federal document with the specified fields.
        """

        # Build the URL.
        full_url = self._build_url(
            endpoint='documents',
            arguments=[document_id]
        )

        if fields == 'all':
            fields = document_fields

        # Define the paramters.
        params = {
            'fields[]': fields
        }

        # Make the request and grab the response.
        response = self._make_request(
            url=full_url,
            method='get',
            params=params
        )

        return response
