"""Textgraph spark tests."""
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


def test_spark_characters():
    """Test spark characters."""
    expected = " ▞▜▘░▒▓▦▷"
    test_values = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    characters = " ▞▜▘░▒▓▦▷"

    spk = textgraph.spark(test_values, characters=characters)
    print("-Spark")
    print(spk)
    print("-Expected")
    print(expected)
    assert spk == expected


def test_spark_char_per_value():
    """Test output of spark_char_per_value."""
    expected = " ▁▂▃▄▅▆▇█"
    test_values = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    spk = textgraph.spark_char_per_value(test_values)
    print("-Spark")
    print(spk)
    print("-Expected")
    print(expected)
    assert spk == expected


def test_spark_per_value_characters():
    """Test spark_char_per_value characters."""
    expected = " ▞▜▘░▒▓▦▷"
    test_values = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    characters = " ▞▜▘░▒▓▦▷"

    spk = textgraph.spark_char_per_value(test_values, characters=characters)
    print("-Spark")
    print(spk)
    print("-Expected")
    print(expected)
    assert spk == expected


def test_spark_char_per_2_values():
    """Test output of spark_char_per_2_values."""
    expected = "⠀⢀⢠⢰⢸⡀⣀⣠⣰⣸⡄⣄⣤⣴⣼⡆⣆⣦⣶⣾⡇⣇⣧⣷⣿"

    test_values = [
        0, 0, 0, 1, 0, 2, 0, 3, 0, 4,
        1, 0, 1, 1, 1, 2, 1, 3, 1, 4,
        2, 0, 2, 1, 2, 2, 2, 3, 2, 4,
        3, 0, 3, 1, 3, 2, 3, 3, 3, 4,
        4, 0, 4, 1, 4, 2, 4, 3, 4, 4,
    ]

    spk = textgraph.spark_char_per_2_values(test_values)
    print("-Spark")
    print(spk)
    print("-Expected")
    print(expected)
    assert spk == expected


def test_spark_per_2_values_characters():
    """Test spark_char_per_2_values characters."""
    expected = "012defabc"
    test_values = [
        0, 0, 0, 1, 0, 2,
        2, 0, 2, 1, 2, 2,
        1, 0, 1, 1, 1, 2,
    ]
    characters = [
        ["0", "1", "2"],
        ["a", "b", "c"],
        ["d", "e", "f"]
    ]

    spk = textgraph.spark_char_per_2_values(test_values, characters=characters)
    print("-Spark")
    print(spk)
    print("-Expected")
    print(expected)
    assert spk == expected
