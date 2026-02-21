# 📈 Options Pricing Engine

A simple web-based tool to estimate the price of an option contract using two industry-standard quantitative finance methods — Black-Scholes and Monte Carlo simulation.

## About Me

I am a Mechatronics Engineering graduate and a postgraduate in Finance from Henley Business School, looking to enter the field of finance in data science, machine learning, or quantitative finance. This project is my attempt to demonstrate my interest and knowledge in the field. I am looking to expand further as I receive new inputs and directions.

Feel free to connect:
- 💼 LinkedIn: [linkedin.com/in/sauravsen34](https://www.linkedin.com/in/sauravsen34)
- 📧 Email: saurav0sen34@gmail.com

---

## What Does This Project Do?

Options pricing is a fundamental problem in quantitative finance — given a set of market inputs, what is the fair price of an option contract today?

This project solves that problem using two methods:

- **Black-Scholes** — a closed-form mathematical formula that gives an instant theoretical price
- **Monte Carlo Simulation** — simulates thousands of possible future stock price paths, calculates the payoff for each, and averages them to estimate the price

The app is fully web-based with interactive sliders and inputs — no coding or installation required to use it.

---

## Inputs

The standard Black-Scholes inputs, controlled via sidebar sliders:

| Input | Symbol | Description |
|-------|--------|-------------|
| Stock Price | S | Current market price of the underlying stock |
| Strike Price | K | The agreed price at which the option can be exercised |
| Time to Maturity | T | Days remaining until the option expires |
| Risk-Free Rate | r | Annual return on a risk-free investment (e.g. UK gilts) |
| Volatility | σ | Expected annualised volatility of the stock |
| Option Type | — | Call (right to buy) or Put (right to sell) |

---

## Outputs

**Option Prices**
- Black-Scholes price
- Monte Carlo price with 95% confidence interval

**The Greeks** — sensitivity measures used by options traders:

| Greek | Symbol | Measures |
|-------|--------|---------|
| Delta | Δ | Price change per £1 move in the stock |
| Gamma | Γ | Rate of change of Delta |
| Vega | ν | Price change per 1% move in volatility |
| Theta | Θ | Daily time decay |
| Rho | ρ | Price change per 1% move in interest rates |

**Chart** — option price plotted across a range of stock prices, with current price and strike price marked.

---

## Project Structure

```
options-pricing-engine/
│
├── app.py              # Streamlit web application
├── requirements.txt    # Python dependencies
├── black_scholes.py    # Black-Scholes formula + d1/d2 computation
├── greeks.py           # Delta, Gamma, Vega, Theta, Rho
└── monte_carlo.py      # Monte Carlo simulation
```

---

## How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/sauravsen3/options-pricing-engine.git
cd options-pricing-engine

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the app
streamlit run app.py
```

---

## Tech Stack

- **Python** — core language
- **NumPy** — numerical computation and random simulation
- **SciPy** — normal distribution functions for Black-Scholes
- **Matplotlib** — charting
- **Streamlit** — interactive web interface

---

*This is part of a series of quantitative finance projects. Next: Portfolio Optimisation Tool.*
