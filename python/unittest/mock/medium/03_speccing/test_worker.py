from unittest import TestCase, expectedFailure, mock

from worker import Helper, Worker


class TestWorker(TestCase):
    def test_patching_class(self):
        # this test will give a false positive
        # there is not `get_path` method but we've mocked it
        with mock.patch("worker.Helper") as MockHelper:
            MockHelper.return_value.get_path.return_value = "testing"
            worker = Worker()
            MockHelper.assert_called_once_with("db")
            self.assertEqual(worker.work(), "testing")

    @expectedFailure
    def test_patching_class_with_spec(self):
        with mock.patch("worker.Helper", autospec=True) as MockHelper:
            # the following would raise attribute error
            # MockHelper.return_value.get_path.return_value = 'testing'
            MockHelper.return_value.get_folder.return_value = "testing"
            worker = Worker()
            MockHelper.assert_called_once_with("db")
            # this test will fail since we're still using `get_path`
            self.assertEqual(worker.work(), "testing")
