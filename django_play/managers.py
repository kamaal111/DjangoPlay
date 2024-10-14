from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any, Generic, TypeVar

import polars as pl
from django.db import connection, models

if TYPE_CHECKING:
    from django_play.typing import PolarsValuesQuerySet

PolarsModel = TypeVar("PolarsModel", bound=models.Model)


class PolarsQuerySet(models.QuerySet):
    def to_polars(self) -> pl.DataFrame:
        return pl.read_database(
            query=self.__parse_sql_statement(),
            connection=connection,
        )

    def __parse_sql_statement(self):
        statement, params = self.query.sql_with_params()

        def map_param(param: Any):
            if isinstance(param, str):
                return f"'{param}'"
            if isinstance(param, datetime):
                return f"'{param.isoformat()}'"

            return param

        return (statement % tuple(map(map_param, params))).__str__()


class PolarsManager(models.Manager.from_queryset(PolarsQuerySet), Generic[PolarsModel]):
    def to_polars(self) -> pl.DataFrame:
        return self.all().to_polars()

    def values(
        self, *fields: str | models.Combinable, **expressions: Any
    ) -> PolarsValuesQuerySet[PolarsModel]:
        return super().values(*fields, **expressions)  # type: ignore
