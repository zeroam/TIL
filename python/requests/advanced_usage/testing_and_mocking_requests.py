import unittest
import requests
import responses


class TestAPI(unittest.TestCase):
    @responses.activate # intercept HTTP calls within this method
    def test_simple(self):
        response_data = {
            'id': 'ch_1GH8so2eZvKYlo2CSMeAfRqt',
            'object': 'charge',
            'custom': {'id': 'cu_1GGwoc2eZvKYlo2CL2m31GRn', 'object': 'customer'},
        }

        # mock the Stripe API
        responses.add(
            responses.GET,
            'https://api.stripe.com/v1/charges',
            json=response_data,
        )

        response = requests.get('https://api.stripe.com/v1/charges')
        self.assertEqual(response.json(), response_data)

    @responses.activate
    def test_connection_error(self):
        with self.assertRaises(requests.exceptions.ConnectionError):
            responses.add(responses.GET, 'https://api.stripe.com/v1/charges')
            response = requests.get('https://invalid-request.com')



if __name__ == '__main__':
    unittest.main()