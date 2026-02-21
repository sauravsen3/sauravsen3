from scipy.stats import norm
import numpy as np

def compute_d1_d2(S, K, T, r, sigma):
    """
    Compute d1 and d2 intermediate values used across Black-Scholes and Greeks.
    
    Returns:
        tuple – (d1, d2)
    """
    d1 = (np.log(S/K) + (r + (sigma**2)/2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - (sigma * np.sqrt(T))
    return d1, d2

def black_scholes_price(S, K, T, r, sigma, option_type="call"):
    """
    Calculate the theoretical price of a European option using Black-Scholes.
    Parameters:
        S           : float – current stock price
        K           : float – strike price
        T           : float – time to expiry in years
        r           : float – annual risk-free rate (e.g. 0.05 = 5%)
        sigma       : float – annual volatility (e.g. 0.20 = 20%)
        option_type : str   – "call" or "put"
    Returns:
        float – option price
    """
    d1, d2 = compute_d1_d2(S, K, T, r, sigma)
    if option_type == "call":
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return round(price, 4)

print(black_scholes_price(S=100, K=100, T=1, r=0.05, sigma=0.20, option_type="call"))
