from src.data import DataLoader, DataCleaner, DataWriter
from src.models import AnalysisEngine
loader = DataLoader()

writer = DataWriter()


df_to_clean = loader.load_data()
cleaner = DataCleaner(df_to_clean)

cleaned_data = cleaner.clean_data()
analyzer = AnalysisEngine(data=cleaned_data)
analyzer.perform_age_segmentation()
analyzer.calculate_lifetime_value()
subset = analyzer.data.head()
subset.to_csv("zortlamalik.csv")