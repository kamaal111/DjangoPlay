from __future__ import annotations

from typing import TYPE_CHECKING, Any, TypeVar

import polars as pl
from django.db import models

if TYPE_CHECKING:
    from django.db.models.query import ValuesQuerySet

PolarsModel = TypeVar("PolarsModel", bound=models.Model)


class PolarsValuesQuerySet(ValuesQuerySet[PolarsModel, dict[str, Any]]):
    def to_polars(self) -> pl.DataFrame: ...
