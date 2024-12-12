import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import os

from csv_operations.csv_operations import CSVFile  # Замените на имя вашего модуля

class TestCSVFile(unittest.TestCase):

    def setUp(self):
        # Создаем временный файл CSV для тестирования
        self.test_file = 'test_data.csv'
        data = {
            'ID': [1, 2],
            'Name': ['John Doe', 'Jane Smith'],
            'Age': [23, 29],
            'City': ['New York', 'Los Angeles'],
            'Occupation': ['Software Engineer', 'Graphic Designer'],
            'Salary': [70000, 65000],
            'Hobby': ['Reading', 'Painting'],
            'Email': ['johndoe@example.com', 'janesmith@example.com']
        }
        pd.DataFrame(data).to_csv(self.test_file, index=False, encoding='utf-8')

    def tearDown(self):
        # Удаляем временный файл после тестов
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_init(self):
        csvf = CSVFile(self.test_file)
        self.assertEqual(csvf.file_name, self.test_file)
        self.assertEqual(csvf.data.shape[0], 2)  # Проверяем, что 2 строки были загружены

    @patch('builtins.input', side_effect=['Alice', '25', 'Los Angeles', 'Student', '50000', 'Surfing', 'alice@example.com'])
    def test_create(self, mock_input):
        csvf = CSVFile(self.test_file)
        csvf.create()

        data = pd.read_csv(self.test_file)
        self.assertEqual(data.shape[0], 3)  # Проверяем, что добавлена новая строка
        self.assertEqual(data.iloc[-1]['Name'], 'Alice')  # Проверяем, что правильное имя добавлено

    def test_get(self):
        csvf = CSVFile(self.test_file)
        result = csvf.get()
        self.assertEqual(result.shape[0], 2)  # Проверяем, что получаем 2 строки

        # Создаем фильтр
        filters = csvf.data['Age'] > 25
        filtered_result = csvf.get(filters)
        self.assertEqual(filtered_result.shape[0], 1)  # Проверяем, что одна строка соответствует фильтру

if __name__ == '__main__':
    unittest.main()
