import pytest

@pytest.fixture
def parser():
    return cli.create_parser()

def test_parser_without_argument(parser):
    """
    Without a arguments parser will exit.
    """

    with pytest.raises(SystemExit):
        parser.parse_args('')

def test_parser_with_argument(parser):
    """
    With a arguments parser will exit.
    """

    with pytest.raises(SystemExit):
        parser.parse_arg([json_file])
