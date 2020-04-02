from unittest import TestCase, expectedFailure, mock

# not importing `pricer`


class TestCountryPrices(TestCase):
    @expectedFailure
    def test_delayed_import(self):
        with mock.patch("pricer.COUNTRIES", ["GB"]):
            from pricer import CountryPricer

            pricer = CountryPricer()
            self.assertAlmostEqual(
                pricer.get_discounted_price(100, "GB"), 80
            )  # Still Fail!
