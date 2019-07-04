"""Textgraph horizontal tests."""
import collections
import textgraph


def test_horizontal():
    """Test basic horizontal output."""
    expected = (
        "\n"
        "████████\n"
        "████████████████\n"
        "███████████████████████\n"
        "███████████████████████████████\n"
        "███████████████████████████████████████\n"
        "███████████████████████████████████████████████\n"
        "███████████████████████████████████████████████████████\n"
        "██████████████████████████████████████████████████████████████\n"
        "██████████████████████████████████████████████████████████████████████\n"
        "██████████████████████████████████████████████████████████████████████████████\n"
    )
    test_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    width = 79

    # Note we force a width here so it doesn't change based on terminal size
    grph = textgraph.horizontal(test_values, width=width)
    print("-Graph")
    print(grph)
    print("-Expected")
    print(expected)
    print("-")
    assert grph == expected


def test_horizontal_labels_tuple():
    """Test labeled horizontal output."""
    expected = (
        "Test0  \n"
        "T1     ████████\n"
        "Test2  ████████████████\n"
        "Test3  ███████████████████████\n"
        "Test4  ███████████████████████████████\n"
        "Test5  ███████████████████████████████████████\n"
        "Test6  ███████████████████████████████████████████████\n"
        "Test7  ███████████████████████████████████████████████████████\n"
        "Test8  ██████████████████████████████████████████████████████████████\n"
        "Test9  ██████████████████████████████████████████████████████████████████████\n"
        "Test10 ██████████████████████████████████████████████████████████████████████████████\n")
    test_values = [
        ('Test0', 0),
        ('T1', 1),
        ('Test2', 2),
        ('Test3', 3),
        ('Test4', 4),
        ('Test5', 5),
        ('Test6', 6),
        ('Test7', 7),
        ('Test8', 8),
        ('Test9', 9),
        ('Test10', 10)
    ]
    width = 79

    # Note we force a width here so it doesn't change based on terminal size
    grph = textgraph.horizontal(test_values, width=width)
    print("-Graph")
    print(grph)
    print("-Expected")
    print(expected)
    print("-")
    assert grph == expected


def test_horizontal_labels_ordereddict():
    """Test labeled horizontal output."""
    expected = (
        "Test0  \n"
        "T1     ████████\n"
        "Test2  ████████████████\n"
        "Test3  ███████████████████████\n"
        "Test4  ███████████████████████████████\n"
        "Test5  ███████████████████████████████████████\n"
        "Test6  ███████████████████████████████████████████████\n"
        "Test7  ███████████████████████████████████████████████████████\n"
        "Test8  ██████████████████████████████████████████████████████████████\n"
        "Test9  ██████████████████████████████████████████████████████████████████████\n"
        "Test10 ██████████████████████████████████████████████████████████████████████████████\n")
    test_values = collections.OrderedDict([
        ('Test0', 0),
        ('T1', 1),
        ('Test2', 2),
        ('Test3', 3),
        ('Test4', 4),
        ('Test5', 5),
        ('Test6', 6),
        ('Test7', 7),
        ('Test8', 8),
        ('Test9', 9),
        ('Test10', 10)
    ])
    width = 79

    # Note we force a width here so it doesn't change based on terminal size
    grph = textgraph.horizontal(test_values, width=width)
    print("-Graph")
    print(grph)
    print("-Expected")
    print(expected)
    print("-")
    assert grph == expected


def test_horizontal_width():
    """Test different width horizontal output."""
    expected = (
        "\n"
        "██\n"
        "████\n"
        "██████\n"
        "████████\n"
        "██████████\n"
        "███████████\n"
        "█████████████\n"
        "███████████████\n"
        "█████████████████\n"
        "███████████████████\n")
    test_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    width = 20

    grph = textgraph.horizontal(test_values, width=width)
    print("-Graph")
    print(grph)
    print("-Expected")
    print(expected)
    print("-")
    assert grph == expected


def test_horizontal_character():
    """Test horizontal character."""
    expected = (
        "\n"
        "◍◍\n"
        "◍◍◍◍\n"
        "◍◍◍◍◍◍\n"
        "◍◍◍◍◍◍◍◍\n"
        "◍◍◍◍◍◍◍◍◍◍\n"
        "◍◍◍◍◍◍◍◍◍◍◍\n"
        "◍◍◍◍◍◍◍◍◍◍◍◍◍\n"
        "◍◍◍◍◍◍◍◍◍◍◍◍◍◍◍\n"
        "◍◍◍◍◍◍◍◍◍◍◍◍◍◍◍◍◍\n"
        "◍◍◍◍◍◍◍◍◍◍◍◍◍◍◍◍◍◍◍\n")
    test_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    width = 20
    character = '◍'

    grph = textgraph.horizontal(test_values, width=width, character=character)
    print("-Graph")
    print(grph)
    print("-Expected")
    print(expected)
    print("-")
    assert grph == expected
