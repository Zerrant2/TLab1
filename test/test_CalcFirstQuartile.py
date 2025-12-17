# -*- coding: utf-8 -*-
from src.Types import DataType
from src.CalcFirstQuartile import CalcFirstQuartile
import pytest

RatingType = dict[str, float]


class TestCalcFirstQuartile:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, RatingType]:
        data: DataType = {
            "Студент 1 (Отличник)": [("m", 100), ("l", 100)],  # avg 100
            "Студент 2 (Хорошист)": [("m", 80), ("l", 80)],  # avg 80
            "Студент 3 (Троечник)": [("m", 60), ("l", 60)],  # avg 60
            "Студент 4 (Двоечник)": [("m", 40), ("l", 40)],  # avg 40
        }

        # Всего 4 студента. Первая квартиль (25%) - это нижние 25%.
        # Сортированные баллы: 40, 60, 80, 100.
        # Индекс 25%: 4 * 0.25 = 1 элемент (это 40).
        # Значит, в первую квартиль попадает только "Двоечник" с баллом 40.
        expected_students: RatingType = {
            "Студент 4 (Двоечник)": 40.0
        }

        return data, expected_students

    def test_calc(self, input_data: tuple[DataType, RatingType]) -> None:
        # Вызываем наш новый класс
        quartile_students = CalcFirstQuartile(input_data[0]).calc()

        # Проверяем, что вернулся именно тот студент
        assert quartile_students == input_data[1]
