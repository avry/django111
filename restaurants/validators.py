from django.core.exceptions import ValidationError
	




CATEGORIES = ['Japanese', 'Indian', 'Western']

def validate_category(value):
	cat = value.capitalize()
	if not value in CATEGORIES and not cat in CATEGORIES:
		raise ValidationError(f"{value} is not valid category")

