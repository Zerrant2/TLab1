# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from src.Types import DataType
from src.DataReader import DataReader


class XMLDataReader(DataReader):
    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        # Открываем и парсим XML файл
        tree = ET.parse(path)
        root = tree.getroot()

        # Проходим по всем элементам <student>
        for student_element in root.findall("student"):
            self.key = student_element.get("name")
            self.students[self.key] = []

            # Проходим по всем предметам внутри студента
            for subject_element in student_element.findall("subject"):
                subj_name = subject_element.get("name")
                # Текст внутри тега может содержать пробелы, чистим его
                score = int(subject_element.text.strip())
                self.students[self.key].append((subj_name, score))

        return self.students