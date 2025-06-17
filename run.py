# run.py

from app import create_app

# Create the Flask app instance using the factory
app = create_app()

if __name__ == '__main__':
    # Run the development server
    app.run(debug=True)
