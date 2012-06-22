from helper import CompatTestCase
from validator.compat import FX14_DEFINITION


class TestFX14Compat(CompatTestCase):
    """Test that compatibility tests for Firefox 14 are properly executed."""

    VERSION = FX14_DEFINITION

    def test_nsIPlacesImportExportService(self):
        """
        nsIPlacesImportExportService.importHTMLFromFile and .importHTMLFromURI
        have both been removed from Gecko 14.
        """
        for method in self.run_xpcom_for_compat(
                "nsIPlacesImportExportService",
                ["importHTMLFromFile", "importHTMLFromURI"]):
            self.assert_silent()
            self.assert_compat_error()

