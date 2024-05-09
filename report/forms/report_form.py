from django import forms
from jalali_date.widgets import AdminSplitJalaliDateTime
from django.contrib.admin.widgets import AdminSplitDateTime

class ReportForm(forms.Form):
    operator_name = forms.CharField(max_length=100)
    start_time = forms.SplitDateTimeField(widget=AdminSplitDateTime)
    end_time = forms.SplitDateTimeField(widget=AdminSplitDateTime)
    production_piece_count = forms.IntegerField()
    defective_piece_count = forms.IntegerField()
    machine = forms.CharField(max_length=500)
    report_text = forms.CharField(max_length=5000, widget=forms.Textarea())
