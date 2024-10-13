from datetime import datetime

import polars as pl
from django.db import connection, models


class PolarsQuerySet(models.QuerySet):
    def to_polars(self):
        statement, params = self.query.sql_with_params()
        corrected_params = []
        for param in params:
            if isinstance(param, str):
                corrected_params.append(f"'{param}'")
            elif isinstance(param, datetime):
                corrected_params.append(f"'{param.isoformat()}'")
            else:
                corrected_params.append(param)

        return pl.read_database(
            query=(statement % tuple(corrected_params)).__str__(), connection=connection
        )


class PolarsManager(models.Manager.from_queryset(PolarsQuerySet)):
    def to_polars(self) -> pl.DataFrame:
        return self.all().to_polars()
