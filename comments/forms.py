from django import forms
from django_comments_xtd.forms import XtdCommentForm as BaseCommentForm

from comments.models import CannedResponse


class CommentForm(BaseCommentForm):

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['email'].initial = 'noreply@example.com'
        self.fields['email'].widget = forms.HiddenInput()

        canned_responses_choices = [(None, '---')]

        canned_responses_choices += ([(canned_response.text, canned_response.text) for canned_response in
                                    CannedResponse.objects.all()])

        self.fields['canned_responses'] = forms.ChoiceField(choices=canned_responses_choices, required=False)

        self.fields['followup'].initial = False
        self.fields['followup'].widget = forms.HiddenInput()

        self.fields['post_anonymously'] = forms.BooleanField(
            label='Don\'t display my username next to my comment', required=False)

    def get_comment_create_data(self, site_id=None):
        data = super().get_comment_create_data(site_id=site_id)

        if self.cleaned_data['canned_responses']:
            data['comment'] = f'{data["comment"]} {self.cleaned_data["canned_responses"]}'

        if self.cleaned_data['post_anonymously']:
            data['user_email'] = ''
            data['user_name'] = 'anonymous'
        return data


class AdminCommentForm(CommentForm):

    def __init__(self, *args, **kwargs):
        super(AdminCommentForm, self).__init__(*args, **kwargs)
        self.is_admin = True
