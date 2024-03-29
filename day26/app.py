from flask import Flask, render_template, request, url_for, redirect
import os
import json

from utils import process_content

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def home():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days Of Python Programming'
    return render_template('home.html', techs=techs, name=name, title='Home')

@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name=name, title='About')

@app.route('/result/<t_words>/<t_chars>/<w_freq>/<m_occur>')
def result(t_words, t_chars, w_freq, m_occur):
    w_freq = json.loads(w_freq)
    print('the word', t_words, t_chars, w_freq, m_occur)
    return render_template('result.html', total_words=t_words, total_characters=t_chars, word_frequency=w_freq, most_occuring_word=m_occur)

@app.route('/post', methods=['GET', 'POST'])
def post():
    name = 'Text Analyzer'
    if request.method == 'GET':
         return render_template('post.html', name=name, title=name)
    if request.method =='POST':
        content = request.form['content']
        total_words, total_characters, word_frequency, most_occuring_word = process_content(content)
        word_frequency = json.dumps(list(word_frequency))
        return redirect(url_for('result', t_words=total_words, t_chars=total_characters, w_freq=word_frequency, m_occur=most_occuring_word))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='127.0.0.1', port=port)
    print('server running')