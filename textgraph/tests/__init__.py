# coding:utf-8
'''
Textgraph Tests
'''
from textgraph.graphs import spark, horizontal_graph, vertical_graph


def test_spark():
    '''
    Test output of spark
    '''
    EXPECTED = u" ▁▂▃▄▅▆▇█"
    TEST_VALUES = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    spk = spark(TEST_VALUES)
    print "-Spark"
    print spk
    print "-Expected"
    print EXPECTED
    assert spk == EXPECTED


def test_horizontal_graph():
    '''
    Test basic horizontal_graph output
    '''
    EXPECTED = (
        u"\n"
        u"████████\n"
        u"████████████████\n"
        u"███████████████████████\n"
        u"███████████████████████████████\n"
        u"███████████████████████████████████████\n"
        u"███████████████████████████████████████████████\n"
        u"███████████████████████████████████████████████████████\n"
        u"██████████████████████████████████████████████████████████████\n"
        u"██████████████████████████████████████████████████████████████████████\n"
        u"██████████████████████████████████████████████████████████████████████████████\n"
    )
    TEST_VALUES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    grph = horizontal_graph(TEST_VALUES)
    print "-Graph"
    print grph
    print "-Expected"
    print EXPECTED
    print "-"
    assert grph.decode('UTF-8') == EXPECTED


def test_horizontal_graph_labels():
    '''
    Test labeled horizontal_graph output
    '''
    EXPECTED = (
        u"Test0  \n"
        u"T1     ████████\n"
        u"Test2  ████████████████\n"
        u"Test3  ███████████████████████\n"
        u"Test4  ███████████████████████████████\n"
        u"Test5  ███████████████████████████████████████\n"
        u"Test6  ███████████████████████████████████████████████\n"
        u"Test7  ███████████████████████████████████████████████████████\n"
        u"Test8  ██████████████████████████████████████████████████████████████\n"
        u"Test9  ██████████████████████████████████████████████████████████████████████\n"
        u"Test10 ██████████████████████████████████████████████████████████████████████████████\n")
    TEST_VALUES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    TEST_LABELS = ['Test0', 'T1', 'Test2', 'Test3', 'Test4', 'Test5', 'Test6',
                   'Test7', 'Test8', 'Test9', 'Test10']

    grph = horizontal_graph(TEST_VALUES, TEST_LABELS)
    print "-Graph"
    print grph
    print "-Expected"
    print EXPECTED
    print "-"
    assert grph.decode('UTF-8') == EXPECTED


def test_horizontal_graph_width():
    '''
    Test different width horizontal_graph output
    '''
    EXPECTED = (
        u"\n"
        u"██\n"
        u"████\n"
        u"██████\n"
        u"████████\n"
        u"██████████\n"
        u"███████████\n"
        u"█████████████\n"
        u"███████████████\n"
        u"█████████████████\n"
        u"███████████████████\n")
    TEST_VALUES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    TEST_WIDTH = 20

    grph = horizontal_graph(TEST_VALUES, width=TEST_WIDTH)
    print "-Graph"
    print grph
    print "-Expected"
    print EXPECTED
    print "-"
    assert grph.decode('UTF-8') == EXPECTED


def test_vertical_graph():
    '''
    Test vertical_graph output
    '''
    EXPECTED = (
        u"          ▉\n"
        u"         ▉▉\n"
        u"        ▉▉▉\n"
        u"       ▉▉▉▉\n"
        u"      ▉▉▉▉▉\n"
        u"     ▉▉▉▉▉▉\n"
        u"    ▉▉▉▉▉▉▉\n"
        u"   ▉▉▉▉▉▉▉▉\n"
        u"  ▉▉▉▉▉▉▉▉▉\n"
        u" ▉▉▉▉▉▉▉▉▉▉\n")
    TEST_VALUES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    grph = vertical_graph(TEST_VALUES)
    print "-Graph"
    print grph
    print "-Expected"
    print EXPECTED
    print "-"
    assert grph.decode('UTF-8') == EXPECTED


def test_vertical_graph_height():
    '''
    Test height of vertical_graph output
    '''
    EXPECTED = (
        u"         ▉▉\n"
        u"       ▉▉▉▉\n"
        u"     ▉▉▉▉▉▉\n"
        u"   ▉▉▉▉▉▉▉▉\n"
        u" ▉▉▉▉▉▉▉▉▉▉\n")
    TEST_VALUES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    TEST_HEIGHT = 5

    grph = vertical_graph(TEST_VALUES, TEST_HEIGHT)
    print "-Graph"
    print grph
    print "-Expected"
    print EXPECTED
    print "-"
    assert grph.decode('UTF-8') == EXPECTED
