from flask import Flask, render_template, request

app = Flask(__name__)
# Doğru cevapları belirleme
correct_answers = {
    'animal': 'balik',
    'color': 'gokyuzu',
    'animals': 'kuş' 
}

@app.route('/')
def quiz():
    return render_template('quizTemplate.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form.get('name', 'Unknown')
        vehicle = request.form.get('vehicle','Not specified')
        animal= request.form.get('animal', 'Not specified')
        color = request.form.get('color', 'Not specified')
        animals = request.form.get('animals', 'Not specified')
        
        total_questions = len(correct_answers)
        points_per_question = 100 / total_questions
        

        # puan hesaplaması
        score = 0 
        if animal.strip().lower() == correct_answers['animal'].lower():
            score += points_per_question
        if color.strip().lower() == correct_answers['color'].lower():
            score += points_per_question
        if animals.strip().lower() == correct_answers['animals'].lower():
            score += points_per_question
       
        
        return f"Thank you {name}, your score is {score:.2f}%.<br>Fatma ATİLAY"
       
   
    except Exception as e:
        return f"An error occurred: {e}"


if __name__ == '__main__':
    app.run(debug=True)
