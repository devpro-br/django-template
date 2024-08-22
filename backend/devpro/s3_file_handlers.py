from storages.backends.s3 import S3Storage


class FileConfigurationError(Exception):
    pass


class S3FileStorage(S3Storage):
    def url(self, name, parameters=None, expire=None, http_method=None):
        url = super().url(name, parameters, expire, http_method)
        if name.startswith('public'):
            url = url.split('?')[0]
        return url

    def get_object_parameters(self, name):
        parameters = super().get_object_parameters(name)
        self._validate(name)
        if self._startswith(name, 'public'):
            parameters['ACL'] = 'public-read'
        else:
            parameters['ACL'] = 'private'
        return parameters

    def _validate(self, name: str):
        if not (self._startswith(name, 'public') or self._startswith(name, 'private')):
            raise FileConfigurationError(f'property "upload_to" must start with "public" or "private" and it is {name}')

    def _startswith(self, name, prefix):
        return name.startswith(f'{self.location}/{prefix}')
