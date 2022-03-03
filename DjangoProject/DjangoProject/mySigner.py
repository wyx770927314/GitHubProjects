from django.core.signing import TimestampSigner


class myTimestampSigner(TimestampSigner):
    def sign(self, value):
        print('sign:'+value)
        return value + 'Test'

    def unsign(self, value, max_age=None):
        print('unsign:'+value)
        return value[0:-4]
