from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False,
                                      db_index=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False,
                                      db_index=True)

    class Meta:
        abstract = True

    def __repr__(self):
        return f"<{self.__class__.__name__} #{self.pk} {self.__str__()}> "
