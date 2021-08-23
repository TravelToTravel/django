from django.http import HttpResponseForbidden

from review.models import Review


def question_ownership_required(func):
    def decorated(request, *args, **kwargs):
        review = Review.objects.get(pk=kwargs['pk'])
        if not review.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated
