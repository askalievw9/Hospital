from .models import Specialty, MedicalRecord
from modeltranslation.translator import TranslationOptions,register

@register(Specialty)
class SpecialtyTranslationOptions(TranslationOptions):
    fields = ('specialty_name',)

@register(MedicalRecord)
class MedicalRecordTranslationOptions(TranslationOptions):
    fields = ('diagnosis', 'treatment', 'prescribed_medication')