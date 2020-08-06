import unittest
import pandas as pd
from lambdata_allan_gon.dataframe_helpers import train_val_test_split as tvts


# to make a test define a class that inherits from
class Test(unittest.TestCase):
    def test_tvts(self):
        """
        Test train_val_test_split
        :return: None
        """
        x = pd.read_csv(
            "https://raw.githubusercontent.com/allan-gon/Unit-2-Build/master/the_model_code/DATA/anime.csv")
        X_train, X_val, X_test, y_train, y_val, y_test = tvts(x, 'genre', .09, .1)
        # Now we make sure the output is as expected with assertions
        self.assertEqual(X_train.shape, (11856, 30))
        self.assertEqual(X_val.shape, (1318, 30))
        self.assertEqual(X_test.shape, (1304, 30))
        self.assertEqual(y_train.shape, (11856,))
        self.assertEqual(y_val.shape, (1318,))
        self.assertEqual(y_test.shape, (1304,))
        return


if __name__ == '__main__':
    unittest.main()
