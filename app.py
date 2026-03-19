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
        return render_template('home.html')
    else:
        try:
            data = CustomData(
                funding_rounds=int(request.form.get('funding_rounds')),
                founder_experience_years=int(request.form.get('founder_experience_years')),
                team_size=int(request.form.get('team_size')),
                market_size_billion=float(request.form.get('market_size_billion')),
                product_traction_users=int(request.form.get('product_traction_users')),
                burn_rate_million=float(request.form.get('burn_rate_million')),
                revenue_million=float(request.form.get('revenue_million')),
                investor_type=request.form.get('investor_type'),
                sector=request.form.get('sector'),
                founder_background=request.form.get('founder_background')
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

            return render_template('home.html',results=predicted_label,raw_prediction=predicted_class)
        except Exception as e:
            return render_template('home.html',error_message=str(e))

if __name__=="__main__":
    app.run(host="0.0.0.0")