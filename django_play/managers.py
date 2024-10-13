import polars as pl
from django.db import connection, models


class PolarsQuerySet(models.QuerySet):
    def to_polars(self):
        return pl.read_database(query=self.query.__str__(), connection=connection)


class PolarsManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return PolarsQuerySet(self.model, using=self._db)
