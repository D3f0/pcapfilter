from unittest.mock import Mock, patch

from pcapfilter.cli import main
from pcapfilter.template import FILTER_TEMPLATE


def test_write_filter_module_template(cli_runner):
    """
    Checks if the -w works
    """
    with patch("builtins.open") as mock_open:
        write = Mock()
        mock_open.return_value.__enter__.return_value.write = write
        retval = cli_runner.invoke(main, ["-w", "/tmp/main.py"])
        mock_open.assert_called_with("/tmp/main.py", "w")
        write.assert_called_with(FILTER_TEMPLATE)
        assert not retval.exception


def test_write_filter_module_incompatible_flags(cli_runner):
    """
    Checks if the -w works
    """

    with patch("builtins.open") as mock_file:
        write = Mock()
        mock_file.return_value.__enter__.return_value.write = write
        cli_runner.invoke(main, ["-rw", "/tmp/main.py"])
        mock_file.assert_not_called()
        write.assert_not_called()


def test_run_filter_receives_module_argument(cli_runner, tmp_path):
    """
    Checks that the python module passed is used
    """

    with patch("pcapfilter.pcapfilter.run_filter") as run_filter:
        module = tmp_path.joinpath("example.py")
        with open(module, "w") as fp:
            fp.write(FILTER_TEMPLATE)
        result = cli_runner.invoke(main, f"-m {module}")
        assert result.exit_code == 0, result.stdout
