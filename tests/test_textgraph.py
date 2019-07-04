# coding:utf-8
"""Textgraph tests."""
import textgraph


def test_spark():
    """Test output of spark."""
    expected = " ▁▂▃▄▅▆▇█"
    test_values = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    spk = textgraph.spark(test_values)
    print("-Spark")
    print(spk)
    print("-Expected")
    print(expected)
    assert spk == expected


def test_horizontal_graph():
    """Test basic horizontal_graph output."""
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

    grph = textgraph.horizontal_graph(test_values)
    print("-Graph")
    print(grph)
    print("-Expected")
    print(expected)
    print("-")
    assert grph == expected


def test_horizontal_graph_labels():
    """Test labeled horizontal_graph output."""
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
    test_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    test_labels = ['Test0', 'T1', 'Test2', 'Test3', 'Test4', 'Test5', 'Test6',
                   'Test7', 'Test8', 'Test9', 'Test10']

    grph = textgraph.horizontal_graph(test_values, labels=test_labels)
    print("-Graph")
    print(grph)
    print("-Expected")
    print(expected)
    print("-")
    assert grph == expected


def test_horizontal_graph_width():
    """Test different width horizontal_graph output."""
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
    test_width = 20

    grph = textgraph.horizontal_graph(test_values, width=test_width)
    print("-Graph")
    print(grph)
    print("-Expected")
    print(expected)
    print("-")
    assert grph == expected


def test_vertical_graph():
    """Test vertical_graph output."""
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

    grph = textgraph.vertical_graph(test_values)
    print("-Graph")
    print(grph)
    print("-Expected")
    print(expected)
    print("-")
    assert grph == expected


def test_vertical_graph_height():
    """Test height of vertical_graph output."""
    expected = (
        "         ▉▉\n"
        "       ▉▉▉▉\n"
        "     ▉▉▉▉▉▉\n"
        "   ▉▉▉▉▉▉▉▉\n"
        " ▉▉▉▉▉▉▉▉▉▉\n")
    test_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    test_height = 5

    grph = textgraph.vertical_graph(test_values, height=test_height)
    print("-Graph")
    print(grph)
    print("-Expected")
    print(expected)
    print("-")
    assert grph == expected
