from flask import Flask,render_template

@app.route('/')
def index():
    files = get_bucket_contents('suvetha')
    return render_template('index.html', files = files)


if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)

        