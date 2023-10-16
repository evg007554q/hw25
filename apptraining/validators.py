from rest_framework.serializers import ValidationError
import re

class urlValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        myString = dict(value).get(self.field, '')
        # myString = 'fdg hfd https://www.youtube.com/ hgjhdfjks https://colab.research.google.com'
        print(myString)

        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', myString)
        # display the extracted URLs
        for url in urls:
            if 'youtube' not in url:
                # print(url)
                raise ValidationError('Можно только youtube')