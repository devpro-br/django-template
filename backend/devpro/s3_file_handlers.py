from django.core.files.storage import FileSystemStorage
from storages.backends.s3 import S3Storage

_PUBLIC_PREFIX = 'public/'
_PRIVATE_PREFIX = 'private/'


class FileConfigurationError(Exception):
    pass


class S3FileStorage(S3Storage):
    def url(self, name, parameters=None, expire=None, http_method=None):
        url = super().url(name, parameters, expire, http_method)
        if name.startswith(_PUBLIC_PREFIX):
            url = url.split('?')[0]
        return url

    def get_object_parameters(self, name):
        parameters = super().get_object_parameters(name)
        self._validate(name)
        if self._startswith(name, _PUBLIC_PREFIX):
            parameters['ACL'] = 'public-read'
        else:
            parameters['ACL'] = 'private'
        return parameters

    def _validate(self, name: str):
        if not (self._startswith(name, _PUBLIC_PREFIX) or self._startswith(name, _PRIVATE_PREFIX)):
            raise FileConfigurationError(f'property "upload_to" must start with "public" or "private" and it is {name}')

    def _startswith(self, name, prefix):
        return name.startswith(f'{self.location}/{prefix}')


class FileSystemWithValidationStorage(FileSystemStorage):
    def _save(self, name, content):
        if not (name.startswith(_PUBLIC_PREFIX) or name.startswith(_PRIVATE_PREFIX)):
            raise FileConfigurationError(f'property "upload_to" must start with "public" or "private" and it is {name}')
        return super()._save(name, content)
