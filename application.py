from flask import Flask, request, render_template
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

@app.route('/', methods=['GET', 'POST'])
def predict():
    final_result = 0
    form_data = {
        'carat': '',
        'depth': '',
        'table': '',
        'x': '',
        'y': '',
        'z': '',
        'cut': '',
        'color': '',
        'clarity': ''
    }

    if request.method == 'POST':
        if 'reset' in request.form:
            # Reset: return empty form and 0 result
            final_result = 0
        elif 'predict' in request.form:
            try:
                # Keep previous input values
                form_data = {key: request.form.get(key, '') for key in form_data}
                data = CustomData(
                    carat=float(form_data['carat']),
                    depth=float(form_data['depth']),
                    table=float(form_data['table']),
                    x=float(form_data['x']),
                    y=float(form_data['y']),
                    z=float(form_data['z']),
                    cut=form_data['cut'],
                    color=form_data['color'],
                    clarity=form_data['clarity']
                )
                final_new_data = data.get_data_as_dataframe()
                predict_pipeline = PredictPipeline()
                pred = predict_pipeline.predict(final_new_data)
                final_result = round(pred[0], 2)
            except Exception as e:
                final_result = f"Error: {str(e)}"

    return render_template('form.html', final_result=final_result, form_data=form_data)


if __name__ == "__main__":
    app.run(debug=True)