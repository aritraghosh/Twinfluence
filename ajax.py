from django.utils import simplejson
@dajaxice_register
def dajaxice_example(request):
    return simplejson.dumps({'message':'Hello World'})
