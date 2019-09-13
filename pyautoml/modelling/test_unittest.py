import unittest

import pandas as pd

from pyautoml import Model


class TestModelling(unittest.TestCase):

    def test_text_gensim_summarize(self):

        text_data = [
                    "Hi my name is PyAutoML. Please split me.",
                    "This function is going to split by sentence. Automation is great."
                    ]

        data = pd.DataFrame(data=text_data, columns=['data'])

        model = Model(data=data, split=False)
        model.summarize_gensim('data', ratio=0.5, run=True)
        validate = model.data_summarized is not None

        self.assertTrue(validate)

    
    def test_text_gensim_keywords(self):

        text_data = [
                    "Hi my name is PyAutoML. Please split me.",
                    "This function is going to split by sentence. Automation is great."
                    ]

        data = pd.DataFrame(data=text_data, columns=['data'])

        model = Model(data=data, split=False)
        model.extract_keywords_gensim('data', ratio=0.5, run=True)
        validate = model.data_extracted_keywords is not None

        self.assertTrue(validate)


    def test_model_getattr(self):

        text_data = [
                    "Hi my name is PyAutoML. Please split me.",
                    "This function is going to split by sentence. Automation is great."
                    ]

        data = pd.DataFrame(data=text_data, columns=['data'])

        model = Model(data=data, split=False)
        model.extract_keywords_gensim('data', ratio=0.5, model_name='model1', run=True)
        validate = model.model1 is not None and model['model1'] is not None

        self.assertTrue(validate)

    def test_model_addtoqueue(self):

        text_data = [
                    "Hi my name is PyAutoML. Please split me.",
                    "This function is going to split by sentence. Automation is great."
                    ]

        data = pd.DataFrame(data=text_data, columns=['data'])

        model = Model(data=data, split=False)
        model.extract_keywords_gensim('data', ratio=0.5, model_name='model1', run=False)
        model.summarize_gensim('data', ratio=0.5, run=False)
        validate = len(model._queued_models)

        self.assertEquals(validate, 2)

    def test_model_kmeans(self):

        data = [[1, 2], [2, 2], [2, 3],
            [8, 7], [8, 8], [25, 80]]

        data = pd.DataFrame(data=data, columns=['col1', 'col2'])

        model = Model(data=data, split=False)
        model.kmeans(n_clusters=3, random_state=0)
        validate = model.kmeans_clusters is not None

        self.assertTrue(validate)

    
    def test_model_kmeans_split(self):

        data = [[1, 2], [2, 2], [2, 3],
            [8, 7], [8, 8], [25, 80]]

        data = pd.DataFrame(data=data, columns=['col1', 'col2'])

        model = Model(data=data)
        model.kmeans(n_clusters=3, random_state=0)
        validate = model.train_data.kmeans_clusters is not None and model.test_data.kmeans_clusters is not None

        self.assertTrue(validate)

    def test_model_dbscan(self):

        data = [[1, 2], [2, 2], [2, 3],
            [8, 7], [8, 8], [25, 80]]

        data = pd.DataFrame(data=data, columns=['col1', 'col2'])

        model = Model(data=data, split=False)
        model.dbscan(eps=3, min_samples=2)
        validate = model.dbscan_clusters is not None

        self.assertTrue(validate)

    def test_model_cluster_filter(self):

        data = [[1, 2], [2, 2], [2, 3],
            [8, 7], [8, 8], [25, 80]]

        data = pd.DataFrame(data=data, columns=['col1', 'col2'])

        model = Model(data=data, split=False)
        model = model.dbscan(eps=3, min_samples=2)
        filtered = model.filter_cluster('dbscan_clusters', 0)
        validate = all(filtered.dbscan_clusters == 0)

        self.assertTrue(validate)

if __name__ == "__main__":
    unittest.main()
