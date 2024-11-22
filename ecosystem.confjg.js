module.exports = {
    apps: [
      {
        name: 'flask-app',
        script: 'gunicorn',
        args: '-w 4 -b 0.0.0.0:5000 nlr_ai:app',
        interpreter: 'python3', // Tell PM2 to use python3
        env: {
          FLASK_APP: 'nlr_ai.py',
          FLASK_ENV: 'production'
        }
      }
    ]
  };
  