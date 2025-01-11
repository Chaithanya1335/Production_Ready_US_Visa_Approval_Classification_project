from us_visa.pipline.training_pipeline import TrainPipeline

obj = TrainPipeline()
data_ingestion_artifact = obj.start_data_ingestion()
#obj.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)