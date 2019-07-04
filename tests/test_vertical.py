"""Textgraph vertical tests."""
import textgraph


def test_vertical():
    """Test vertical output."""
    expected = (
        "          ▉\n"
        "         ▉▉\n"
        "        ▉▉▉\n"
        "       ▉▉▉▉\n"
        "      ▉▉▉▉▉\n"
        "     ▉▉▉▉▉▉\n"
        "    ▉▉▉▉▉▉▉\n"
        "   ▉▉▉▉▉▉▉▉\n"
        "  ▉▉▉▉▉▉▉▉▉\n"
        " ▉▉▉▉▉▉▉▉▉▉\n")
    test_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    grph = textgraph.vertical(test_values)
    print("-Graph")
    print(grph)
    print("-Expected")
    print(expected)
    print("-")
    assert grph == expected


def test_vertical_height():
    """Test height of vertical output."""
    expected = (
        "         ▉▉\n"
        "       ▉▉▉▉\n"
        "     ▉▉▉▉▉▉\n"
        "   ▉▉▉▉▉▉▉▉\n"
        " ▉▉▉▉▉▉▉▉▉▉\n")
    test_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    test_height = 5

    grph = textgraph.vertical(test_values, height=test_height)
    print("-Graph")
    print(grph)
    print("-Expected")
    print(expected)
    print("-")
    assert grph == expected


def test_vertical_character():
    """Test vertical character."""
    expected = (
        "         ◊◊\n"
        "       ◊◊◊◊\n"
        "     ◊◊◊◊◊◊\n"
        "   ◊◊◊◊◊◊◊◊\n"
        " ◊◊◊◊◊◊◊◊◊◊\n")
    test_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    height = 5
    character = "◊"

    grph = textgraph.vertical(test_values, height=height, character=character)
    print("-Graph")
    print(grph)
    print("-Expected")
    print(expected)
    print("-")
    assert grph == expected
