import polars as pl
from django.db import connection, models


class PolarsQuerySet(models.QuerySet):
    def to_polars(self):
        statement, params = self.query.sql_with_params()
        corrected_params = []
        for param in params:
            if not isinstance(param, str):
                corrected_params.append(param)
            else:
                corrected_params.append(f"'{param}'")

        return pl.read_database(
            query=(statement % tuple(corrected_params)).__str__(), connection=connection
        )


class PolarsManager(models.Manager.from_queryset(PolarsQuerySet)):
    def to_polars(self) -> pl.DataFrame:
        return self.all().to_polars()
