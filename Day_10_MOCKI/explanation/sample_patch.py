import os


class RemovalService:
    """A service for removing objects from the filesystem."""

    def rm(self, filename):
        os.remove(filename)

    def file_exists(self, path):
        return os.path.exists(path)


if __name__ == '__main__':
    reference = RemovalService()
    print(reference.file_exists(r'C:\Development\Python\pytest-sample\sample_4_mocks\explanation\sample_patch.py'))
