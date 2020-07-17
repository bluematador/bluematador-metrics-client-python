import unittest

import bluematador

class TestSum(unittest.TestCase):
    def test_sanitize_metric(self):
        '''
        Sanitize illegal metric name
        '''
        bm = bluematador.BlueMatadorClient()

        sanitized_metric_name = bm.sanitize('my.app:new', ':')
        self.assertEqual('my.app_new', sanitized_metric_name)

        sanitized_metric_name = bm.sanitize('my.app|new', ':')
        self.assertEqual('my.app_new', sanitized_metric_name)

    def test_sanitize_labels(self):
        '''
        Sanitize illegal label names
        '''
        bm = bluematador.BlueMatadorClient()

        sanitized_labels = bm.sanitize_labels({'env': '#dev', 'account|id': '1234'})
        self.assertEqual('_dev', sanitized_labels['env'])
        self.assertEqual('1234', sanitized_labels['account_id'])

if __name__ == '__main__':
    unittest.main()
