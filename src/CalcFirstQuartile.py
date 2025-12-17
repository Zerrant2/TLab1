# -*- coding: utf-8 -*-
from src.Types import DataType
from src.CalcRating import CalcRating

# Определяем тип для словаря рейтингов: Имя -> Балл
RatingType = dict[str, float]


class CalcFirstQuartile:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating: RatingType = {}

    def calc(self) -> RatingType:
        # Сначала считаем средний рейтинг всех студентов
        # используем уже готовый класс CalcRating
        full_rating = CalcRating(self.data).calc()

        # Собираем все баллы в список и сортируем их
        values = sorted(full_rating.values())

        # Если студентов нет, возвращаем пустоту
        if not values:
            return {}

        # Вычисляем порог первой квартили (25%)
        # Это элемент, стоящий на позиции 25% от длины списка
        # Например, если 4 студента, то index = 1 (второй по счету, если округлять вверх)
        # Упрощенная формула: q1_index = len(values) // 4
        # Если нужно более точное (математическое) вычисление:
        import math
        q1_index = math.ceil(len(values) * 0.25) - 1

        # Защита от отрицательного индекса
        if q1_index < 0:
            q1_index = 0

        q1_value = values[q1_index]

        # Фильтруем студентов: берем тех, у кого рейтинг <= q1_value
        filtered_students: RatingType = {}
        for student, rating in full_rating.items():
            if rating <= q1_value:
                filtered_students[student] = rating

        return filtered_students