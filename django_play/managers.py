from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any, Generic, TypeVar

import polars as pl
from django.db import connection, models

if TYPE_CHECKING:
    from django.db.models.query import ValuesQuerySet

PolarsModel = TypeVar("PolarsModel", bound=models.Model)


class PolarsQuerySet(models.QuerySet):
    def to_polars(self) -> pl.DataFrame:
        statement, params = self.query.sql_with_params()

        def map_param(param: Any):
            if isinstance(param, str):
                return f"'{param}'"
            if isinstance(param, datetime):
                return f"'{param.isoformat()}'"

            return param

        return pl.read_database(
            query=(statement % tuple(map(map_param, params))).__str__(),
            connection=connection,
        )


class PolarsManager(models.Manager.from_queryset(PolarsQuerySet), Generic[PolarsModel]):
    def to_polars(self) -> pl.DataFrame:
        return self.all().to_polars()

    def values(
        self, *fields: str | models.Combinable, **expressions: Any
    ) -> ValuesQuerySet[PolarsModel, dict[str, Any]]:
        return super().values(*fields, **expressions)
