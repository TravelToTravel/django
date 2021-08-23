from django.forms import ModelForm

from review.models import Review


class ReviewCreationForm(ModelForm):
    class Meta:
        model = Review
        fields = ['subject', 'image', 'content']

        labels = {
            'subject': '제목',
            'image': '이미지',
            'content': '내용',
        }
