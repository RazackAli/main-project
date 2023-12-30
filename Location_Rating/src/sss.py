from flask import Flask, render_template

app = Flask(__name__)


# Route for the home page
@app.route('/')
def home():
    # Location information
    location = {
        'name': 'New York City',
        'latitude': 40.7128,
        'longitude': -74.0060
    }

    # Road information
    roads = [
        {
            'name': 'Broadway',
            'length': '13 miles'
        },
        {
            'name': '5th Avenue',
            'length': '6 miles'
        },
        {
            'name': 'Park Avenue',
            'length': '4 miles'
        }
    ]

    # Render the template with location and road information
    return render_template('map.html', location=location, roads=roads)


if __name__ == '__main__':
    app.run(debug=True)
