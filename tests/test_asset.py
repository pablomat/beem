import unittest
from steem import Steem
from steem.asset import Asset
from steem.instance import set_shared_steem_instance
from steem.exceptions import AssetDoesNotExistsException


class Testcases(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.bts = Steem(
            nobroadcast=True,
        )
        set_shared_steem_instance(self.bts)

    def test_assert(self):
        with self.assertRaises(AssetDoesNotExistsException):
            Asset("FOObarNonExisting", full=False)

    def test_refresh(self):
        asset = Asset("1.3.0", full=False)
        asset.ensure_full()
        self.assertIn("dynamic_asset_data", asset)
        self.assertIn("flags", asset)
        self.assertIn("permissions", asset)
        self.assertIsInstance(asset["flags"], dict)
        self.assertIsInstance(asset["permissions"], dict)

    def test_properties(self):
        asset = Asset("1.3.0", full=False)
        self.assertIsInstance(asset.symbol, str)
        self.assertIsInstance(asset.precision, int)
        self.assertIsInstance(asset.is_bitasset, bool)
        self.assertIsInstance(asset.permissions, dict)
        self.assertEqual(asset.permissions, asset["permissions"])
        self.assertIsInstance(asset.flags, dict)
        self.assertEqual(asset.flags, asset["flags"])

    """
    # Mocker comes from pytest-mock, providing an easy way to have patched objects
    # for the life of the test.
    def test_calls(mocker):
        asset = Asset("USD", lazy=True, steem_instance=Steem(offline=True))
        method = mocker.patch.object(Asset, 'get_call_orders')
        asset.calls
        method.assert_called_with(10)
    """