from checklistos.core.apps import CoreConfig


def test_app():
    assert CoreConfig.name == 'core'
