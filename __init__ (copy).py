def maintain(summary,date,start_time,end_time,email1,email2,description,location):
    now = datetime.now()
    today = date.today()
    data = {}
    data['details'].append({
        'Summary': summary,
        'Date' : date,
        'S_Time' : start_time,
        'E_Time' : end_time,
    }),
    data['invites'].append({
        '1_Invite' : email1,
        '2_Invite' : email2,
        '3_Invite' : email3,
        '4_Invite' : email4,
    }),
    data['extra'].append({
        'Description' : description,
        'Location' : location,
    }),
    data['record'].append({
        'R_Date' : today.strftime("%B %d, %Y"),
        'R_Time' : now.strftime("%H:%M:%S"),
    })
    with open('records.json', 'w') as outfile:
        json.dump(data, outfile)

    @app.route('/history')
    @login_required(username=['admin'])
    def history():
        if os.path.exists('records.json'):
            data = []
            with open('records.json', 'r') as f:
                data = json.load(f)
                f.close()
            return render_template('history.html', history=data)
        else:
            return render_template('failed.html')
        # elif(username is not 'admin'):
        #     return render_template('failed.html')

<img src="{{ url_for('static', filename='images/3.png') }}" class="navlogo">
<img src="{{ url_for('static', filename='images/2.png') }}" class="navimg">

<div class="container">
<footer>
{% block footer %}
    <address>
    Written by <a href="mailto:webmaster@example.com">Jon Doe</a>.<br>
    Visit us at: Example.com Box 564, Disneyland USA<br>
    Copyright 1996
    </address>
{% endblock %}
</footer>
</div>

{{ history.details }}{{ history.invites }}{{ history.extra }}{{ history.record }}

@app.route('/secret')
@login_required()
def secret():
    return render_template('secret.html')

@app.route('/add_event', methods=['POST'])

    @app.route('/home')
    @app.route('/index')

,email2,email3,email4,email5
email2="",email3="",email4="",email5="",

@app.errorhandler(404)
def not_found():
    """Page not found."""
    return render_template("error.html", message="Page Not Found")

@app.errorhandler(400)
def bad_request():
    """Bad request."""
    return render_template("error.html", message="Bad Request")

@app.errorhandler(500)
def server_error():
    """Internal server error."""
    return render_template("error.html", message="Internal Server Error")

{% for ingredient in history %}
<td>{{ history.details }}</td>
<td>{{ history.invites }}</td>
<td>{{ history.extra }}</td>
<td>{{ history.record }}</td>
{% endfor %}

def maintain(summary,date,start_time,end_time,email1,email2,description,location,response):

    # today = date.today()
    data = []
    data['details'].append({
        'Summary': summary,
        'Date' : date,
        'S_Time' : start_time,
        'E_Time' : end_time,
    }),
    data['invites'].append({
        '1_Invite' : email1,
        '2_Invite' : email2,
        # '3_Invite' : email3,
        # '4_Invite' : email4,
    }),
    data['extra'].append({
        'Description' : description,
        'Location' : location,
    }),
    data['record'].append({
        'R_Date' : now.strftime("%B %d, %Y"),
        'R_Time' : now.strftime("%H:%M:%S"),
        'Response':response,
    })
    with open('records.json', 'w') as outfile:
        json.dump(data, outfile)

{% block tail%}
  <script src="http://cdnjs.cloudflare.com/ajax/libs/lodash.js/2.4.1/lodash.js"></script>
  <script src="script.js"></script>
{% endblock %}
