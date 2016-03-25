# daily-dashboard
A Flask app I built for myself to show me information that I want to see each day.

## Configuration
Place a `.daily-dashboard` file in your home directory. 

In it, add your developer API key for Forecast.io. It should be JSON-formatted, as such:

    {"api_key":"my_api_key_here"}

Note to self: use double-quotes, not single-quotes!

## Running the App

    python dashboard.py