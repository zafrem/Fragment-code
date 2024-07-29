#pip install unittest


# external_service.py
class ExternalService:
    def fetch_data(self):
        # 외부 서비스에서 데이터를 가져오는 복잡한 작업을 수행
        pass

class DataProcessor:
    def __init__(self, service):
        self.service = service

    def process(self):
        data = self.service.fetch_data()
        return f"Processed {data}"

# test_data_processor.py
import unittest
from unittest.mock import Mock
#from external_service import ExternalService, DataProcessor

class TestDataProcessor(unittest.TestCase):

    def test_process(self):
        mock_service = Mock(spec=ExternalService)
        mock_service.fetch_data.return_value = "mock data"

        processor = DataProcessor(mock_service)
        result = processor.process()

        self.assertEqual(result, "Processed mock data")
        mock_service.fetch_data.assert_called_once()


if __name__ == '__main__':
    unittest.main()