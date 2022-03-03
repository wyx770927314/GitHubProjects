from django.core.files.uploadedfile import TemporaryUploadedFile
from django.core.files.uploadhandler import *


class MyFileUploadHandler(TemporaryFileUploadHandler):
    def new_file(self, *args, **kwargs):
        super(MyFileUploadHandler, self).new_file(*args, **kwargs)
        print('This is my FileUploadHandler-----This is my FileUploadHandler-----This is my FileUploadHandler')
        self.file = TemporaryUploadedFile(self.file_name, self.content_type, 0, self.charset, self.content_type_extra)

