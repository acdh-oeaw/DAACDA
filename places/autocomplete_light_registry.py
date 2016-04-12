from autocomplete_light import shortcuts as al

from labels.models import Label

class NameAutocomplete(al.AutocompleteModelBase):

	search_fields=['label']
	model = Label
	attrs = {
        'data-autocomplete-minimum-characters': 2,
        'placeholder': 'Start typing to get suggestions',
    }

al.register(Label, NameAutocomplete)

