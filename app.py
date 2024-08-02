from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import CustomData, PredictPipeline


application = Flask(__name__)

# Route for home page (landing page)
@application.route('/')
def home():
    return render_template('home.html')

@application.route("/predict-data", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template('home.html')
    else:
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=int(request.form.get('reading_score')),
            writing_score=int(request.form.get('writing_score'))
        )

        pred_df = data.get_data_as_dataframe()
        print(pred_df)

        # Load the trained model
        pipeline = PredictPipeline()
        results = pipeline.predict(pred_df)
        return render_template("home.html", results=results[0]) 

if __name__ == '__main__':
    application.run(host="0.0.0.0")
