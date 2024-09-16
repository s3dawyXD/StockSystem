```
this README FILE WAS Created by the help of ChatGPT

```

# StockSystem

**StockSystem** is a Django-based application designed to manage the stock of ingredients for a restaurant's product offerings. Specifically, the system is built to track ingredients used in burgers and automatically update inventory after customer orders. Additionally, the system sends email alerts to the merchant when ingredient levels fall below a set threshold, helping to ensure inventory is replenished before it runs out.

---

## Features

- Manage products (e.g., burgers) and their associated ingredients.
- Track ingredient stock in real-time, updated automatically with each order.
- Send low-stock email alerts when any ingredient falls below 50% of the initial stock.
- Prevent multiple low-stock email alerts for the same ingredient once the 50% threshold is crossed.
- Easily expandable to accommodate additional products, ingredients, or custom stock levels.

---

## Project Structure

### Models

- **Ingredient**: Stores individual ingredients like beef, cheese, and onion, along with their current stock levels.
- **Product**: Represents a product (like a burger) that consists of various ingredients in specific amounts.
- **ProductIngredient**: A through model that links a product with its ingredients and the amount of each ingredient required.
- **Order**: Records customer orders and automatically updates stock levels when an order is created.

### Views

- **OrderViewSet**: Accepts customer order data via a POST request, creates the order, updates ingredient stock levels, and sends email alerts if stock falls below 50%.

---

## Installation Instructions

### Requirements

Ensure you have the following installed on your system:

- Python 3.8+
- Django 4.x
- SQLite (or other database configurations like PostgreSQL if preferred)
- An email backend (e.g., SMTP) to send email notifications

### Steps to Install

#### You can Run the app Using Docker-compose

1. Clone the repository:
   ```bash
   git clone https://github.com/s3dawyXD/StockSystem.git
   cd StockSystem
   ```
2. Run
   ```bash
   Docker compose up
   ```

#### OR Normal Running

1. Clone the repository:

   ```bash
   git clone https://github.com/s3dawyXD/StockSystem.git
   cd StockSystem

   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run database migrations:
   ```bash
   python manage.py migrate
   ```
4. Seed the initial data for ingredients and products:
   ```bash
   python manage.py loaddata initial_data.json
   ```
5. set your `.env` file as `.env_example`
6. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Future Enhancements

- add views to update ingredients stock
- add extra data in order model like (created_by, barch, etc..)
- add user model and activate the authentication module
