from flask import Flask,request,render_template
from src.pipelines.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html', form_data={})
    else:
        form_data = request.form.to_dict()
        try:
            data = CustomData(
                funding_rounds=int(form_data.get('funding_rounds')),
                founder_experience_years=int(form_data.get('founder_experience_years')),
                team_size=int(form_data.get('team_size')),
                market_size_billion=float(form_data.get('market_size_billion')),
                product_traction_users=int(form_data.get('product_traction_users')),
                burn_rate_million=float(form_data.get('burn_rate_million')),
                revenue_million=float(form_data.get('revenue_million')),
                investor_type=form_data.get('investor_type'),
                sector=form_data.get('sector'),
                founder_background=form_data.get('founder_background')
            )
            pred_df=data.get_data_as_data_frame()
            print(pred_df)
            print("Before Prediction")
            predict_pipeline=PredictPipeline()
            print("Mid Prediction")
            results=predict_pipeline.predict(pred_df)
            print("After Prediction")

            predicted_class=int(results[0])
            label_map={
                0: "Acquisition",
                1: "Failure",
                2: "IPO"
            }
            predicted_label=label_map.get(predicted_class,f"Unknown ({predicted_class})")

            return render_template('home.html',results=predicted_label,raw_prediction=predicted_class, form_data=form_data)
        except Exception as e:
            return render_template('home.html',error_message=str(e), form_data=form_data)

if __name__=="__main__":
    app.run(host="0.0.0.0")