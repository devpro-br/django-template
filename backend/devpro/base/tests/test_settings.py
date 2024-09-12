import pytest

from devpro import settings


@pytest.fixture
def settings_empty_bucket():
    settings.configure_storage(False)
    return settings


def test_no_s3_configured_for_files(settings_empty_bucket):
    settings_empty_bucket.AWS_STORAGE_BUCKET_NAME = ''
    assert settings_empty_bucket.STORAGES['default'][
               'BACKEND'] == 'devpro_s3_storages.handlers.FileSystemWithValidationStorage'


def test_no_s3_configured_for_static(settings_empty_bucket):
    settings.AWS_STORAGE_BUCKET_NAME = ''
    assert settings.STORAGES['staticfiles']['BACKEND'] == 'django.contrib.staticfiles.storage.StaticFilesStorage'


@pytest.fixture
def settings_with_bucket():
    settings.configure_storage(True)
    return settings


def test_s3_configured_for_files(settings_with_bucket):
    assert settings.STORAGES['default']['BACKEND'] == 'devpro_s3_storages.handlers.S3FileStorage'


def test_s3_configured_for_static(settings_with_bucket):
    settings_with_bucket.AWS_STORAGE_BUCKET_NAME = 'somebucket'
    assert settings_with_bucket.STORAGES['staticfiles'][
               'BACKEND'] == 'storages.backends.s3.S3Storage'
