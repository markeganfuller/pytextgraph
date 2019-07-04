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
