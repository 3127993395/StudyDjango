from django.core.files.uploadhandler import *
from django.core.files.uploadedfile import *
class myFileUploadHander(TemporaryFileUploadHandler):
    def new_file(self, *args, **kwargs):
        super().new_file(*args, **kwargs)
        print('This is my FileUploadHander')
        self.file = TemporaryUploadedFile(self.file_name, self.content_type, 0, self.charset, self.content_type_extra)