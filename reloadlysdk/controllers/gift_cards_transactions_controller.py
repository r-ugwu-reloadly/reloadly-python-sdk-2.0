# -*- coding: utf-8 -*-

"""
reloadlysdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from reloadlysdk.api_helper import APIHelper
from reloadlysdk.configuration import Server
from reloadlysdk.controllers.base_controller import BaseController
from reloadlysdk.exceptions.api_exception import APIException


class GiftCardsTransactionsController(BaseController):

    """A Controller to access Endpoints in the reloadlysdk API."""
    def __init__(self, config):
        super(GiftCardsTransactionsController, self).__init__(config)

    def reloadly_gift_cards_transactions(self,
                                         accept,
                                         authorization,
                                         size=None,
                                         page=None,
                                         start_date=None,
                                         end_date=None):
        """Does a GET request to /reports/transactions.

        TODO: type endpoint description here.

        Args:
            accept (string): TODO: type description here.
            authorization (string): TODO: type description here.
            size (string, optional): This indicates the number of transactions
                to be retrieved on a page.
            page (string, optional): This indicates the page of the
                transactions list being retrieved.
            start_date (string, optional): Indicates the start date for the
                range of transactions to be retrieved.
            end_date (string, optional): Indicates the end date for the range
                of transactions to be retrieved.

        Returns:
            mixed: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/reports/transactions'
        _query_builder = self.config.get_base_uri(Server.GIFT_CARDS)
        _query_builder += _url_path
        _query_parameters = {
            'size': size,
            'page': page,
            'startDate': start_date,
            'endDate': end_date
        }
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder,
            _query_parameters
        )
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Accept': accept,
            'Authorization': authorization
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 401:
            raise APIException('Full authentication is required to access this resource', _response)
        elif _response.status_code == 404:
            raise APIException('Could not retrieve/update resources at the moment, please try again later', _response)
        self.validate_response(_response)
        if (_response.text is not None) or (not str(_response.text)):
            decoded = APIHelper.json_deserialize(_response.text)

        return decoded

    def reloadly_gift_cards_transaction_by_id(self,
                                              accept,
                                              authorization,
                                              transactionid):
        """Does a GET request to /reports/transactions/{transactionid}.

        TODO: type endpoint description here.

        Args:
            accept (string): TODO: type description here.
            authorization (string): TODO: type description here.
            transactionid (string): Indicates the identification number of the
                transaction to be retrieved.

        Returns:
            mixed: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/reports/transactions/{transactionid}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'transactionid': {'value': transactionid, 'encode': True}
        })
        _query_builder = self.config.get_base_uri(Server.GIFT_CARDS)
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'Accept': accept,
            'Authorization': authorization
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 401:
            raise APIException('Indicates the identification number of the transaction to be retrieved.', _response)
        elif _response.status_code == 404:
            raise APIException('Could not retrieve/update resources at the moment, please try again later', _response)
        self.validate_response(_response)
        if (_response.text is not None) or (not str(_response.text)):
            decoded = APIHelper.json_deserialize(_response.text)

        return decoded
