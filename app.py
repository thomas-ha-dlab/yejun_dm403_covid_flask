from flask import Flask, render_template
import corona_data
import corona_area

# 플라스크 앱 생성
app = Flask(__name__)

# URL 라우터 설정
@app.route('/')
def index():
    data = corona_data.get_corona_summary()
    city_data = corona_area.get_city_data()
    print("국내 데이터", data)
    print("시도 데이터", city_data)

    # return "인덱스 페이지"
    return render_template('index.html', corona_data=data, corona_city=city_data)

# 메인 코드
if __name__ == "__main__":
    app.run(debug=True)